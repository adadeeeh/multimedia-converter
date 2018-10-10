from PIL import Image

WIDTH = 'width'
HEIGHT = 'height'
COLOR_DEPTH = 'color_depth'
CONVERSION_RATE = 'conversion_rate'
OUTPUT = 'output'


def convert(source, output, args):
    im = Image.open(source)
    if WIDTH in args and HEIGHT in args:
        im = im.resize((int(args[WIDTH]), int(args[HEIGHT])))
    if COLOR_DEPTH in args:
        im = im.convert('P', palette=Image.ADAPTIVE, colors=int(args[COLOR_DEPTH])).convert('RGB')
    if CONVERSION_RATE in args:
        pass
    im.save(output, args[OUTPUT])
    return 0
