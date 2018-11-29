import os
import time

import requests
from flask import *
from werkzeug import exceptions

from common import util, mistserver
from convert import video, image, audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = util.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB

ms = mistserver.MistServer()
AUDIO_EXTENSIONS = ('mp3', 'wmv')
VIDEO_EXTENSIONS = ('mp4', 'mkv')

@app.route('/')
def home():
    return render_template('index.html')

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
        file = request.files.get('file')
        if name and file:
            filename = ms.save(file)
            addstream = ms.api({'addstream': {name: {"source": filename}}})
            streams = addstream['streams']
            if streams.get('incomplete list') == 1 and name in streams:
                if filename.endswith(AUDIO_EXTENSIONS):
                    return redirect('/streaming/audio')
                elif filename.endswith(VIDEO_EXTENSIONS):
                    return redirect('/streaming/video')
            raise exceptions.InternalServerError('Failed to add stream')
        raise exceptions.BadRequest('\'name\' and/or \'file\' are not valid')


def streamer(template_name, extensions):
    ms_api = ms.api()
    streams = [v for k, v in ms_api['streams'].items() if v['source'].endswith(extensions)]
    return render_template(template_name, streams=streams, mistserver_host=ms.HOST)


@app.route('/streaming/audio')
def streaming_audio():
    return streamer('streaming/audio.html', AUDIO_EXTENSIONS)


@app.route('/streaming/video')
def streaming_video():
    return streamer('streaming/video.html', VIDEO_EXTENSIONS)


@app.route('/info_<path:stream_name>.js')
def secure_stream_info(stream_name):
    """
    endpoint to rewrite http to https in info_<stream_name>.js file which
    have http:// scheme defined in all its urls.
    :param stream_name: stream name
    :return: same .js file with http replaced to https
    """
    info = requests.get('%s:8081/info_%s.js' % (ms.HOST, stream_name)).text
    return info.replace('http:', 'https:')


if __name__ == '__main__':
    app.run(debug=True)
