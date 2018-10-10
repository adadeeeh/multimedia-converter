import subprocess

ffmpeg_params = {
    'bitrate': 'b',
    'sample_rate': 'ar',
    # 'channel': 'r',
}


def convert(source, output, args):
    command = 'ffmpeg -i %s' % source
    for key in args:
        if ffmpeg_params.get(key):
            command += ' -%s %s' % (ffmpeg_params[key], str(args[key]))
    command += ' %s' % output
    return subprocess.call(command.split())
