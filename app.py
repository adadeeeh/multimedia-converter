import json
import os

from flask import Flask, render_template, request, send_from_directory, abort, url_for, Response, send_file

from common import util
from convert import video, image, audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = util.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/files/<path:filename>')
def files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def wrap_request(converter_function):
    try:
        filename = util.save_uploaded_file(request.files['file'])
        source = util.get_temp_path(filename)
        output = util.get_output_path(filename, request.values['output'])
        result = converter_function(source, output, request.values)
        os.remove(source)
        if result == 0:
            if 'json' in request.args and request.args == True:
                return Response(json.dumps({
                    'status': 'success',
                    'file_url': url_for('files', filename=util.get_filename(filename, request.values['output']))
                }), mimetype='application/json')
            else:
                return send_file(output)
    except KeyError:
        pass
    abort(400)


@app.route('/api/convert/image', methods=['POST'])
def convert_image():
    return wrap_request(image.convert)


@app.route('/api/convert/audio', methods=['POST'])
def convert_audio():
    return wrap_request(audio.convert)


@app.route('/api/convert/video', methods=['POST'])
def convert_video():
    return wrap_request(video.convert)


if __name__ == '__main__':
    app.run()
