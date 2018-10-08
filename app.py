from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/convert/image', methods=['POST'])
def convert_image():
    pass


@app.route('/api/convert/audio', methods=['POST'])
def convert_audio():
    pass


@app.route('/api/convert/video', methods=['POST'])
def convert_video():
    pass


if __name__ == '__main__':
    app.run()
