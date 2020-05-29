#!/bin/bash

rm -f dark/*.html
cp *.html dark/.
python3 dark.py dark/*.html
