#!/usr/bin/env python

import sys
import os
import code
from pathlib import Path

with open('template/header.html', 'r', encoding='utf8') as file:
    header = file.readlines()

with open('template/footer.html', 'r', encoding='utf8') as file:
    footer = file.readlines()


def whitespace(a):
    count = len(a) - len(a.lstrip(' '))
    return a[0:count]


def search_and_replace(path):

    with open(path, 'r', encoding='utf8') as file:
        content = file.readlines()

    out = []

    for line in content:
        if line.strip().startswith('<header>'):
            space = whitespace(line)
            out.append(space + '<header>\n')
            for h in header:
                out.append(space + '  ' + h)
            out.append(space + '</header>\n')
        elif line.strip().startswith('<footer>'):
            space = whitespace(line)
            out.append(space + '<footer>\n')
            for f in footer:
                out.append(space + '  ' + f)
            out.append(space + '</footer>\n')
        elif line.strip().startswith('<pre>'):
            space = whitespace(line)
            out.append(space + '<pre><code>')
            source = line.lstrip(' ').lstrip('<pre>').rstrip('</pre>\n')
            out.append(code.highlight(source) + '</code></pre>\n')
        else:
            out.append(line)

    content = "".join(out)
    content = content.replace('<!--this-->', path)

    with open(path, 'w', encoding='utf8') as file:
        file.write(content)


for path in sys.argv:
    if path.endswith('.html'):
        search_and_replace(path)
