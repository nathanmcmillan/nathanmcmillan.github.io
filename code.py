import os
import re
import json
import html

directory = 'code/'
syntax_directory = 'code/syntax/'


class Rule:
    def __init__(self, pattern, replace):
        self.pattern = re.compile(pattern)
        self.replace = replace

    def sub(self, line):
        return self.pattern.sub(self.replace, line)


def c_syntax(source):
    rules = []
    with open(syntax_directory + 'c.json', 'r') as f:
        d = json.load(f)
        for e in d:
            s = d[e]
            rules.append(Rule(e, s))
    out = []
    # TODO
    # Iterate through list of rules until a match is found, them substring line and repeat
    # Do not end line until no matches are found on the remainder

    # TODO
    # Escape lines to html before processing
    # Also transform regex to HTML first

    for line in source:
        end = ''
        while True:
            for rule in rules:
                line = rule.sub(line)
                match = 2
                line = line[2:]
                continue
            break
        # line = html.escape(line)
        end += liine
        out.append(end)
    return ''.join(out)


def highlight(name):
    with open(directory + name, 'r') as file:
        source = file.readlines()
    base = os.path.basename(name)
    ext = os.path.splitext(base)[1]
    if ext == '.c':
        return c_syntax(source)
    return ''.join(source)
