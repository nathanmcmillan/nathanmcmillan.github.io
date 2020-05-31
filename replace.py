import sys
import re


def search_and_replace(path):
    with open(path, 'r') as file:
        content = file.read()

    content = content.replace('href="light.css"', 'href="dark.css"')
    content = content.replace('href="resume.css"', 'href="resume_dark.css"')
    content = content.replace('title="dark color scheme"', 'title="light color scheme"')
    content = content.replace('src="moon-solid.svg"', 'src="sun-solid.svg"')

    regex = re.compile(r'href="(.*)\.html"')
    content = regex.sub(r'href="\g<1>_dark.html"', content)

    regex = re.compile(r'href="(.*)_dark_dark\.html"')
    content = regex.sub(r'href="\g<1>.html"', content)

    with open(path, 'w') as file:
        file.write(content)


for path in sys.argv:
    if path.endswith('.html'):
        search_and_replace(path)
