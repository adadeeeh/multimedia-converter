import PIL
from PIL import Image

WIDTH = 'width'
HEIGHT = 'height'
COLOR_MODE = 'color_mode'
COLOR_DEPTH = 'color_depth'
ROTATE = 'rotate'
EXPAND_ROTATE = 'expand_rotate'
TRANSPOSE = 'transpose'
CONVERSION_RATE = 'conversion_rate'
OUTPUT = 'output'

flip_mode = {
    'left_right': PIL.Image.FLIP_LEFT_RIGHT,
    'top_bottom': PIL.Image.FLIP_TOP_BOTTOM,
    'rotate_90': PIL.Image.ROTATE_90,
    'rotate_180': PIL.Image.ROTATE_180,
    'rotate_270': PIL.Image.ROTATE_270,
    'transpose': PIL.Image.TRANSPOSE
}


def convert(source, output, args):
    im: Image.Image = Image.open(source)
    if args.get(WIDTH) and args.get(HEIGHT):
        im = im.resize((int(args[WIDTH]), int(args[HEIGHT])))
    if args.get(COLOR_DEPTH):
        im = im.convert('P', palette=Image.ADAPTIVE, colors=int(args[COLOR_DEPTH])).convert('RGB')
    if args.get(ROTATE):
        expand = bool(args.get(EXPAND_ROTATE)) or False
        im = im.rotate(int(args.get(ROTATE)), expand=expand)
    if args.get(COLOR_MODE):
        im = im.convert(args.get(COLOR_MODE))
    if flip_mode.get(args.get(TRANSPOSE)):
        im = im.transpose(flip_mode.get(args.get(TRANSPOSE)))
    if args.get(CONVERSION_RATE):
        pass
    im.save(output, args[OUTPUT])
    return 0
