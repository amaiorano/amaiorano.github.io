# Notes

## Setup

Install Ruby (without Devkit): https://www.ruby-lang.org/en/

Install Jekyll: https://jekyllrb.com/
gem install bundler jekyll

cd amaiorano.github.io
bundle install
serve.bat

## Delete unreferenced images

Easier to download all images into a folder under assets\images\<folder>, write up the post, then run tools\delete-unreferenced-images.py to automatically delete the unreferenced images (they get moved to a temporary directory that's output to stdout).


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

## Order posts on the same day

Add a 'date' field to the front matter, set the correct date, but for the time, set 12:00:0n and make n = 0, 1, 2, etc.
