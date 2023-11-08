import os
import re
import glob
import tempfile
import shutil
import argparse
from pathlib import Path
from os import path

parser = argparse.ArgumentParser(
    prog='delete-unreferenced-images',
    description='Deletes images not referenced in post from the image directory' +
        ' (note: images are moved to a temporary directory, not actually deleted)'
)
parser.add_argument('post_path', help=f"path to post markdown file (e.g. {os.path.join('_posts', 'mypost.md')})")
parser.add_argument('image_dir', help=f"path to image directory (e.g. {os.path.join('assets', 'images', 'mypost')})")
args = parser.parse_args()

post = args.post_path
img_dir = args.image_dir

def abs_resolve_path(p):
    return str(Path(path.abspath(p)).resolve())

script_path = path.dirname(os.path.realpath(__file__))
root_path = path.abspath(path.join(script_path, '..'))

# Find files referenced by post
post_files = set()
for line in open(post):
    m = re.match(r'\!\[\]\((.*)\)', line)
    if m:
        img_file = m.groups()[0]
        post_files.add(abs_resolve_path(root_path + path.sep + img_file))

# Find all files in img_dir
all_files = set([abs_resolve_path(f) for f in glob.glob(img_dir + path.sep + "**/*.*", recursive=True)])

# print("post_files: {}\n".format(post_files))
# print("all_files: {}\n".format(all_files))

# Get list of unreferenced files
unreferenced_files = all_files - post_files

print('Total files:        {}'.format(len(all_files)))
print('Post files:         {}'.format(len(post_files)))
print('Unreferenced files: {}'.format(len(unreferenced_files)))

if len(all_files) - len(post_files) != len(unreferenced_files):
    raise Exception('Error! Too many files to delete! (all_files - post_files != unreferenced_files)')

# print('Delete:')
# for f in unreferenced_files:
#     print(f)

if len(unreferenced_files) == 0:
    print('No unreferenced files found.')
else:
    temp_dir = tempfile.mkdtemp(prefix='blog_deleted_files_')

    print('Moving unreferenced files to {}'.format(temp_dir))
    for f in unreferenced_files:
        shutil.move(f, temp_dir)
