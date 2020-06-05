import os
import re

directory = 'code'


def c_syntax(source):
    return ''.join(source)


def highlight(name):
    with open(directory + '/' + name, 'r') as file:
        source = file.readlines()
    base = os.path.basename(name)
    ext = os.path.splitext(base)[1]
    if ext == 'c':
        return c_syntax(source)
    return ''.join(source)
