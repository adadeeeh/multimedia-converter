from PIL import Image

RESOLUTION = 'resolution'
COLOR_DEPTH = 'color_depth'
CONVERSION_RATE = 'conversion_rate'
OUTPUT = 'output'


def convert(source, output, args):
    im = Image.open(source)
    if RESOLUTION in args:
        width, height = tuple(args[RESOLUTION].split('x'))
        im = im.resize((int(width), int(height)))
    if COLOR_DEPTH in args:
        im = im.convert(colors=args[COLOR_DEPTH])
    if CONVERSION_RATE in args:
        pass
    im.save(output, args[OUTPUT])
    return 0