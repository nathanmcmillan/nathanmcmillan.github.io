#!/bin/bash -eu

css='css'

rm -rf $css

mkdir $css

cp template/dark.min.css $css/dark.css
cp template/light.min.css $css/light.css

echo "" >> $css/dark.css
echo "" >> $css/light.css

cat template/style.css >> $css/dark.css
cat template/style.css >> $css/light.css

cp template/resume.light.min.css $css/resume.css
cp template/resume.dark.min.css $css/resume_dark.css

echo "" >> $css/resume.css
echo "" >> $css/resume_dark.css

cat template/resume.style.css >> $css/resume.css
cat template/resume.style.css >> $css/resume_dark.css

cp template/code.css $css/code.css
