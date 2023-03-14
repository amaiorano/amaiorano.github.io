import argparse
import pyperclip
from os import path, listdir
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='clip-markdown-image-links',
    description='Scans images in directory and copies markdown-formatted links to the clipboard'
)
parser.add_argument('image_dir', help=f"path to image directory (e.g. {path.join('assets', 'images', 'mypost')})")
args = parser.parse_args()

img_dir = args.image_dir

script_path = path.dirname(path.realpath(__file__))
root_path = path.abspath(path.join(script_path, '..'))

image_path = Path(root_path, args.image_dir)
image_files = [Path(image_path, f) for f in listdir(image_path)]

# example:
# 1
# ![](/assets/images/snes-2-chip-rgb-filter-mod/IMG_7712.jpg)
#
text = ''
for i,f in enumerate(image_files):
    # Format relative path to image for markdown
    rel_path = '/' + path.relpath(f, root_path).replace('\\', '/')
    text += f'{i}\n'
    text += f'![]({rel_path})\n'
    text += f'\n'

print(text)
pyperclip.copy(text)

print('\n\nCopied to clipboard!')