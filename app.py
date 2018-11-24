import os
import time

import requests
from flask import Flask, render_template, request, send_from_directory, abort, url_for, redirect
from werkzeug.utils import secure_filename

from common import util
from convert import video, image, audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = util.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 50 MB

MISTSERVER_FOLDER = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], 'mistserver'))
AUDIO_EXTENSIONS = ('mp3', 'wmv')
VIDEO_EXTENSIONS = ('mp4', 'mkv')


@app.route('/convert/audio')
def hello_world():
    return render_template('convert/audio.html')


@app.route('/convert/image')
def image_route():
    return render_template('convert/image.html')


@app.route('/convert/video')
def video_route():
    return render_template('convert/video.html')


@app.route('/convert/files/<path:filename>')
def files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def converter(converter_function):
    start_time = time.time()
    filename = util.save_uploaded_file(request.files['file'], request.values.get('filename'))
    source = util.get_temp_path(filename)
    output = util.get_output_path(filename, request.values['output'])
    result = converter_function(source, output, request.values)
    os.remove(source)
    print('Execution time: %d' % ((time.time() - start_time) * 1000))
    if result == 0:
        return redirect(url_for('files', filename=util.get_filename(filename, request.values['output'])))
    abort(400)


@app.route('/api/convert/image', methods=['POST'])
def convert_image():
    return converter(image.convert)


@app.route('/api/convert/audio', methods=['POST'])
def convert_audio():
    return converter(audio.convert)


@app.route('/api/convert/video', methods=['POST'])
def convert_video():
    return converter(video.convert)


@app.route('/streaming/add', methods=['GET', 'POST'])
def add_stream():
    if request.method == 'GET':
        return render_template('streaming/add.html')
    else:
        name = request.values.get('name')
        file = request.files['file']
        filename = os.path.join(MISTSERVER_FOLDER, secure_filename(file.filename))
        file.save(filename)
        addstream = requests.get(
            'http://localhost:4242/api?command={"addstream": {"%s": {"source": "%s"}}}' % (name, filename)).json()
        streams = addstream['streams']
        print(streams)
        if streams['incomplete list'] == 1 and name in streams:
            if filename.endswith(AUDIO_EXTENSIONS):
                return redirect('/streaming/audio')
            elif filename.endswith(VIDEO_EXTENSIONS):
                return redirect('/streaming/video')
        abort(400)


def streamer(template_name, extensions, stream_name):
    ms_api = requests.get('http://localhost:4242/api').json()
    filtered = {k: v for k, v in ms_api['streams'].items() if v['source'].endswith(extensions)}
    if stream_name and stream_name not in filtered:
        raise abort(404)
    streams = [v for k, v in filtered.items()]
    return render_template(template_name, streams=streams, stream_name=stream_name)


@app.route('/streaming/audio', defaults={'stream_name': None})
@app.route('/streaming/audio/<path:stream_name>')
def streaming_audio(stream_name):
    return streamer('streaming/audio.html', AUDIO_EXTENSIONS, stream_name)


@app.route('/streaming/video', defaults={'stream_name': None})
@app.route('/streaming/video/<path:stream_name>')
def streaming_video(stream_name):
    return streamer('streaming/video.html', VIDEO_EXTENSIONS, stream_name)


if __name__ == '__main__':
    app.run()
