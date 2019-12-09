# Notes

## Setup

Install Ruby (without Devkit): https://www.ruby-lang.org/en/

Install Jekyll: https://jekyllrb.com/
gem install bundler jekyll

cd amaiorano.github.io
bundle install
serve.bat

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
