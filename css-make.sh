#!/bin/bash -eu

rm -rf css/*

cat template/light.min.css template/style.css > css/index.css
cat template/resume.light.min.css template/resume.css > css/resume.css

rm -rf dark/css/*

cat template/dark.min.css template/style.css > dark/css/index.css
cat template/resume.dark.min.css template/resume.css > dark/css/resume.css
