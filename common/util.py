import os
import uuid

UPLOAD_FOLDER = '.files'
TEMP_EXTENSION = 'tmp'
MISTSERVER_FOLDER = os.path.abspath(os.path.join(UPLOAD_FOLDER, 'mistserver'))
MISTSERVER_API = (os.environ.get('MISTSERVER_HOST') or 'localhost:4242') + '/api'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

if not os.path.exists(MISTSERVER_FOLDER):
    os.mkdir(MISTSERVER_FOLDER)


def generate_filename():
    return str(uuid.uuid4())


def save_uploaded_file(file, filename=''):
    filename = filename or generate_filename()
    file.save(get_temp_path(filename))
    return filename


def get_filename(filename, extension):
    return '%s.%s' % (filename, extension)


def get_temp_filename(filename):
    return get_filename(filename, TEMP_EXTENSION)


def get_temp_path(filename):
    return os.path.join(UPLOAD_FOLDER, get_temp_filename(filename))


def get_output_path(filename, extension):
    return os.path.join(UPLOAD_FOLDER, get_filename(filename, extension))
