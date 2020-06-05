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
    for line in source:
        for rule in rules:
            line = rule.sub(line)
        # line = html.escape(line)
        out.append(line)
    return ''.join(out)


def highlight(name):
    with open(directory + name, 'r') as file:
        source = file.readlines()
    base = os.path.basename(name)
    ext = os.path.splitext(base)[1]
    if ext == '.c':
        return c_syntax(source)
    return ''.join(source)
