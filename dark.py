import sys


def search_and_replace(path):
    with open(path, 'r') as file:
        content = file.read()
    content = content.replace('light.css', 'dark.css')
    with open(path, 'w') as file:
        file.write(content)


for path in sys.argv:
    if path.endswith('.html'):
        search_and_replace(path)
