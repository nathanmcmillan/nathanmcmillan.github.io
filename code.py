import sys
import re


def search_and_replace(path):
    with open(path, 'r') as file:
        content = file.read()

    # regex = re.compile(r'href="(.*)\.html"')
    # content = regex.sub(r'href="\g<1>_dark.html"', content)

    content = content.replace('const', '<span class="c-const">const</span>')
    content = '<pre>' + content + '</pre>'

    with open(path, 'w') as file:
        file.write(content)


for path in sys.argv:
    if path.endswith('.html'):
        search_and_replace(path)
