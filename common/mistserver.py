import os

import requests
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename

from common import util


class MistServer:
    def __init__(self, host=None, username=None, password=None):
        self.MEDIA_FOLDER = os.environ.get('MISTSERVER_MEDIA_FOLDER') or '/mistserver/media'
        self.HOST = host or os.environ.get('MISTSERVER_HOST') or 'http://127.0.0.1'
        if not self.HOST.startswith('http://') and not self.HOST.startswith('https://'):
            self.HOST = 'http://' + self.HOST
        self.USERNAME = username or os.environ.get('MISTSERVER_USERNAME')
        self.PASSWORD = password or os.environ.get('MISTSERVER_PASSWORD')
        self.challenge = None

    def get_password(self):
        if not self.challenge:
            return self.PASSWORD
        return util.encode_md5(util.encode_md5(self.PASSWORD), self.challenge)

    def build_authorization(self):
        if not self.challenge:
            return {}

        if not self.USERNAME or not self.PASSWORD:
            raise BadRequest('A challenge is required but no username and/or password is provided')

        return {'authorize': {'username': self.USERNAME, 'password': self.get_password()}}

    def build_command(self, command):
        cmd = command.copy()
        cmd.update(self.build_authorization())
        if cmd:
            cmd = '?command=' + str(cmd)
        else:
            cmd = ''
        return cmd

    def build_url(self, command):
        return '%s:4242/api%s' % (self.HOST, self.build_command(command))

    def request(self, command):
        return requests.get(self.build_url(command)).json()

    def save(self, file):
        os.makedirs(self.MEDIA_FOLDER, exist_ok=True)
        filename = self.MEDIA_FOLDER + '/' + secure_filename(file.filename)
        file.save(filename)
        return filename

    def api(self, command=None):
        if command is None:
            command = {}
        response = self.request(command)

        if response['authorize']['status'] == 'CHALL':
            self.challenge = response['authorize']['challenge']
            response = self.request(command)

            if response['authorize']['status'] != 'OK':
                raise BadRequest('Username and/or password provided for MistServer are not valid')

        response['streams'] = response.get('streams') or dict()
        return response
