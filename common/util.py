import os
import uuid

UPLOAD_FOLDER = '.files'
TEMP_EXTENSION = 'tmp'


def generate_filename():
    return str(uuid.uuid4())


def save_uploaded_file(file):
    filename = generate_filename()
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
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
