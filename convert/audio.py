import subprocess

TIME_OFF = 'time_off'
TIME_OFF_H = 'time_off_h'
TIME_OFF_M = 'time_off_m'
TIME_OFF_S = 'time_off_s'
TIME_STOP = 'time_stop'
TIME_STOP_H = 'time_stop_h'
TIME_STOP_M = 'time_stop_m'
TIME_STOP_S = 'time_stop_s'

DISABLE_AUDIO = 'disable_audio'

ffmpeg_params = {
    'time_off': 'ss',
    'time_stop': 'to',
    'bitrate_audio': 'b:a',
    'sample_rate': 'ar',
    'channels': 'ac',
    'volume': 'vol'
}


def convert(source, output, args):
    print(args)
    command = 'ffmpeg -i %s' % source
    for key in args:
        if args.get(key) and ffmpeg_params.get(key):
            command += ' -%s %s' % (ffmpeg_params[key], str(args[key]))
    if args.get(TIME_OFF_H) and args.get(TIME_OFF_M) and args.get(TIME_OFF_S) and not args.get(TIME_OFF):
        command += ' -ss %s:%s:%s' % (args[TIME_OFF_H], args[TIME_OFF_M], args[TIME_OFF_S])
    if args.get(TIME_STOP_H) and args.get(TIME_STOP_M) and args.get(TIME_STOP_S) and not args.get(TIME_STOP):
        command += ' -to %s:%s:%s' % (args[TIME_STOP_H], args[TIME_STOP_M], args[TIME_STOP_S])
    if args.get(DISABLE_AUDIO):
        command += ' -an'
    command += ' %s' % output
    print(command)
    return subprocess.call(command.split())
