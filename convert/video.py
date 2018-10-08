import subprocess

ffmpeg_params = {
    'frame_size': 's',
    'frame_rate': 'r',
    'bitrate': 'b',
    'sample_rate': 'ar',
    # 'channel': 'r',
}


def convert(source, output, args):
    command = 'ffmpeg -i %s' % source
    for key in args:
        if key in ffmpeg_params:
            command += ' -%s %s' % (ffmpeg_params[key], str(args[key]))
    command += ' %s' % output
    return subprocess.call(command.split())
