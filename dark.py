#!/usr/bin/env python

import sys
import re

css = '/css/'


def search_and_replace(path):
    with open(path, 'r', encoding='utf8') as file:
        content = file.read()

    content = content.replace('href="'+css+'light.css"', 'href="'+css+'dark.css"')
    content = content.replace('href="'+css+'resume.css"', 'href="'+css+'resume_dark.css"')
    content = content.replace('title="dark color scheme"', 'title="light color scheme"')

    regex = re.compile(r'href="([^"]*?)\.html"')
    content = regex.sub(r'href="/dark\g<1>.html"', content)

    regex = re.compile(r'href="/dark/dark/dark([^"]*?)\.html"')
    content = regex.sub(r'href="\g<1>.html"', content)

    with open(path, 'w', encoding='utf8') as file:
        file.write(content)


for path in sys.argv:
    if path.endswith('.html'):
        search_and_replace(path)
