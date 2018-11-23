import os
import time

from flask import Flask, render_template, request, send_from_directory, abort, url_for, redirect

from common import util
from convert import video, image, audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = util.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 10 MB


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


if __name__ == '__main__':
    app.run()
