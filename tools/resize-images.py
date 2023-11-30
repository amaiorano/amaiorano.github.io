import argparse
from os import path, listdir
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser(
    prog='resize-images',
    description='Resizes images down to input dimensions while maintaining aspect ratio'
)
parser.add_argument('image_dir', help=f"path to image directory (e.g. {path.join('assets', 'images', 'mypost')})")
parser.add_argument('--width', help=f"width", type=int, default=1024)
parser.add_argument('--height', help=f"height", type=int, default=768)
args = parser.parse_args()

img_dir = args.image_dir
width = args.width
height = args.height

script_path = path.dirname(path.realpath(__file__))
root_path = path.abspath(path.join(script_path, '..'))

image_path = Path(root_path, args.image_dir)
image_files = [Path(image_path, f) for f in listdir(image_path)]

for f in image_files:
    try:
        im = Image.open(f)
        if im.width > width or im.height > height:
            print(f'Resizing to {width}x{height}: {f}')
            im.thumbnail((width, height), Image.LANCZOS)
            im.save(f)
        else:
            print(f'Skipping resize: {f}')
    except IOError:
        print(f'Cannot resize {f}')
