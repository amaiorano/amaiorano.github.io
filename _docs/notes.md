# Notes

## Resize images

```
sudo apt-get install imagemagick 
mogrify -path . -resize 1024x768 *.jpg
```

## Fix image orientation

```
sudo apt install imagemagick
find . \( -iname '*.jpg' -o  -iname '*.png' \) -exec convert -auto-orient {} {} \;
```
