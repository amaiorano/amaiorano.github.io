# Notes

## Fix image orientation

sudo apt install jhead
jhead -v -norot IMG_7386.jpg

For some reason, rotating image clockwise from what it should be, and then running jhead -norot seems to do the trick.

## Resize images

sudo apt-get install imagemagick 
mogrify -path . -resize 1024x768 *.jpg
