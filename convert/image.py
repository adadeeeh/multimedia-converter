from PIL import Image

WIDTH = 'width'
HEIGHT = 'height'
COLOR_DEPTH = 'color_depth'
CONVERSION_RATE = 'conversion_rate'
OUTPUT = 'output'


def convert(source, output, args):
    im = Image.open(source)
    if args.get(WIDTH) and args.get(HEIGHT):
        im = im.resize((int(args[WIDTH]), int(args[HEIGHT])))
    if args.get(COLOR_DEPTH):
        im = im.convert('P', palette=Image.ADAPTIVE, colors=int(args[COLOR_DEPTH])).convert('RGB')
    if args.get(CONVERSION_RATE):
        pass
    im.save(output, args[OUTPUT])
    return 0
