# Delete unreferenced images
# Usage: delete-unreferenced-images.py <path_to_post> <path_to_images_root>

import sys
import os
import re
import glob
import tempfile
import shutil
from pathlib import Path
from os import path

post = sys.argv[1]
img_dir = sys.argv[2]

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
all_files = set([abs_resolve_path(f) for f in glob.glob(img_dir + path.sep + "*.*", recursive=False)])

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

temp_dir = tempfile.mkdtemp(prefix='blog_deleted_files_')

print('Moving unreferenced files to {}'.format(temp_dir))
for f in unreferenced_files:
    shutil.move(f, temp_dir)
