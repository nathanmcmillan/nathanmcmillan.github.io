import sys
import re

css = '/css/'
svg = '/svg/'


def search_and_replace(path):
    with open(path, 'r') as file:
        content = file.read()

    content = content.replace('href="'+css+'light.css"', 'href="'+css+'dark.css"')
    content = content.replace('href="'+css+'resume.css"', 'href="'+css+'resume_dark.css"')
    content = content.replace('title="dark color scheme"', 'title="light color scheme"')
    content = content.replace('src="/svg/'+svg+'moon-solid.svg"', 'src="'+svg+'sun-solid.svg"')

    regex = re.compile(r'href="/dark([^"]*?)\.html"')
    content = regex.sub(r'href="<!--dark-->\g<1>.html"', content)

    regex = re.compile(r'href="([^"]*?)\.html"')
    content = regex.sub(r'href="/dark\g<1>.html"', content)

    regex = re.compile(r'href="<!--dark-->([^"]*?)\.html"')
    content = regex.sub(r'href="\g<1>.html"', content)

    with open(path, 'w') as file:
        file.write(content)


for path in sys.argv:
    if path.endswith('.html'):
        search_and_replace(path)
