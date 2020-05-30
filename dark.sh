#!/bin/bash

rm *.dark.html

for f in *.html; do
  d="$(basename $f .html).dark.html"
  cp $f $d
done

python3 dark.py *.dark.html

rm dark.css
rm light.css

cp dark.min.css dark.css
cp light.min.css light.css

echo "" >> dark.css
echo "" >> light.css

cat common.css >> dark.css
cat common.css >> light.css
