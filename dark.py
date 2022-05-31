#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
import re

def dark_search_and_replace(content):
    content = content.replace('>Dark<', '>Light<')
    content = content.replace('href="/', 'href="/dark/')
    content = content.replace('href="/dark/dark/dark', 'href="')
    return content
