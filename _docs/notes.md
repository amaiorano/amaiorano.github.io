# Notes

## Fix image orientation

sudo apt install jhead

First run with -autorot on the image:

jhead -autorot IMG_7386.jpg

Then, rotate the image using whatever photo editor (Photos App on Windows). For some reason, rotating the image clockwise from what it should be seems to do the trick.

## Resize images

sudo apt-get install imagemagick 
mogrify -path . -resize 1024x768 *.jpg

