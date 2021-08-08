#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import os.path
import re
import json
import html

directory = 'code/'
syntax_directory = 'code/syntax/'


class Rule:
    def __init__(self, info):
        try:
            self.pattern = re.compile(info[0])
        except Exception as e:
            print(info[0], e)
        self.capture = info[1]

    def surround(self, match, line):
        out = ''
        groups = len(match.groups()) + 1
        if groups != len(self.capture):
            raise Exception('Capture groups were not the same as match groups')
        for i in range(groups):
            span = self.capture[i]
            if span is None:
                continue
            group = match.group(i)
            out += '<' + span + '>' + html.escape(group) + '</' + span + '>'
            if i > 0 and i < groups-1:
                between = line[match.end(i):match.start(i+1)]
                out += html.escape(between)
        if groups > 1:
            out += line[match.end(groups-1):match.end(0)]
        return out


def syntax(syntax_file, source):
    rules = []
    with open(syntax_file, 'r', encoding='utf8') as f:
        d = json.load(f)
        d = d["syntax"]
        for e in d:
            rules.append(Rule(e))
    out = []

    for line in source:
        end = ''
        while True:
            best = None
            for rule in rules:
                match = rule.pattern.search(line)
                if match is None:
                    continue
                if best is None:
                    best = (rule, match)
                else:
                    dif = match.start(0) - best[1].start(0)
                    if dif < 0 or (dif == 0 and match.end(0) > best[1].end(0)):
                        best = (rule, match)
            if best is None:
                break
            rule = best[0]
            match = best[1]
            out += html.escape(line[0:match.start(0)]) + rule.surround(match, line)
            line = line[match.end(0):]
        end += html.escape(line)
        out.append(end)

    return ''.join(out)


def highlight(name):
    with open(directory + name, 'r', encoding='utf8') as file:
        source = file.readlines()
    base = os.path.basename(name)
    ext = os.path.splitext(base)[1]
    ext = ext[1:]
    syntax_file = syntax_directory + ext + '.json'
    if os.path.isfile(syntax_file):
        return syntax(syntax_file, source)
    return ''.join(source)
