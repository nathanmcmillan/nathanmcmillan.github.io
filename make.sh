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

css='docs/css'

rm -rf $css

mkdir $css

cp template/dark.min.css $css/dark.css
cp template/light.min.css $css/light.css

echo "" >> $css/dark.css
echo "" >> $css/light.css

cat template/common.css >> $css/dark.css
cat template/common.css >> $css/light.css

cp template/resume.light.min.css $css/resume.css
cp template/resume.dark.min.css $css/resume_dark.css

echo "" >> $css/resume.css
echo "" >> $css/resume_dark.css

cat template/resume.common.css >> $css/resume.css
cat template/resume.common.css >> $css/resume_dark.css
