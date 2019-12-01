# Notes

## Fix image orientation

Download exiftool: https://exiftool.org

Remove orientation info from EXIF metadata for all images:

exiftool.exe -Orientation= -n -overwrite_original *

## Resize images

sudo apt-get install imagemagick 
mogrify -path . -resize 1024x768 *.jpg

