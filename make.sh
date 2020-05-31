#!/bin/bash

rm *.html

cp pages/*.html .

python3 template.py *.html

for f in *.html; do
  d="$(basename $f .html)_dark.html"
  cp $f $d
done

python3 replace.py *_dark.html

rm dark.css
rm light.css

cp template/dark.min.css dark.css
cp template/light.min.css light.css

echo "" >> dark.css
echo "" >> light.css

cat template/common.css >> dark.css
cat template/common.css >> light.css

rm resume.css
rm resume_dark.css

cp template/resume.light.min.css resume.css
cp template/resume.dark.min.css resume_dark.css

echo "" >> resume.css
echo "" >> resume_dark.css

cat template/resume.common.css >> resume.css
cat template/resume.common.css >> resume_dark.css
