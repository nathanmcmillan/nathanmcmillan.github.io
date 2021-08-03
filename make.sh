#!/bin/bash -eu

rm -f *.html

rm -rf dark
rm -rf articles

mkdir dark

cp -r html/* .
cp -r html/* dark

./template.py *.html

function template {
  find "$1" -name '*.html' -print0 | while IFS= read -r -d '' f; do
    ./template.py $f
  done
}

template articles
template dark

find dark -name '*.html' -print0 | while IFS= read -r -d '' f; do
  ./dark.py $f
done

./css-make.sh
