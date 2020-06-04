#!/bin/bash -eu

rm -rf docs/dark

find docs -name '*.html' -print0 | while IFS= read -r -d '' f; do
  rm $f
done

mkdir docs/dark

cp -r pages/* docs
cp -r pages/* docs/dark

find docs -name '*.html' -print0 | while IFS= read -r -d '' f; do
  python3 template.py $f
done

find docs/dark -name '*.html' -print0 | while IFS= read -r -d '' f; do
  python3 dark.py $f
done

./css-make.sh
