import subprocess

WIDTH = 'width'
HEIGHT = 'height'
SIZE = 'size'

TIME_OFF = 'time_off'
TIME_OFF_H = 'time_off_h'
TIME_OFF_M = 'time_off_m'
TIME_OFF_S = 'time_off_s'
TIME_STOP = 'time_stop'
TIME_STOP_H = 'time_stop_h'
TIME_STOP_M = 'time_stop_m'
TIME_STOP_S = 'time_stop_s'

DISABLE_AUDIO = 'disable_audio'
DISABLE_VIDEO = 'disable_video'

ffmpeg_params = {
    'time_off': 'ss',
    'time_stop': 'to',
    'rate': 'r',
    'size': 's',
    'aspect': 'aspect',
    'disable_video': 'vn',
    'bitrate_video': '-b:v',
    'bitrate_audio': '-b:a',
    'sample_rate': 'ar',
    'channels': 'ac',
    'disable_audio': 'an',
    'volume': 'vol'
}


def convert(source, output, args):
    command = 'ffmpeg -i %s' % source
    for key in args:
        if args.get(key) and ffmpeg_params.get(key):
            command += ' -%s %s' % (ffmpeg_params[key], str(args[key]))
    if args.get(WIDTH) and args.get(HEIGHT) and not args.get(SIZE):
        command += ' -s %sx%s' % (args[WIDTH], args[HEIGHT])
    if args.get(TIME_OFF_H) and args.get(TIME_OFF_M) and args.get(TIME_OFF_S) and not args.get(TIME_OFF):
        command += ' -ss %s:%s:%s' % (args[TIME_OFF_H], args[TIME_OFF_M], args[TIME_OFF_S])
    if args.get(TIME_STOP_H) and args.get(TIME_STOP_M) and args.get(TIME_STOP_S) and not args.get(TIME_STOP):
        command += ' -to %s:%s:%s' % (args[TIME_STOP_H], args[TIME_STOP_M], args[TIME_STOP_S])
    if args.get(DISABLE_AUDIO):
        command += '-an'
    if args.get(DISABLE_VIDEO):
        command += '-vn'
    command += ' -f %s' % output
    return subprocess.call(command.split())
