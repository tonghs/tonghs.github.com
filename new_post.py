#!/usr/bin/env python
# coding: utf-8

import sys
import datetime


template = """---
published: true
layout: post
---
"""


def main(title):
    t = datetime.date.today()
    if not title:
        title = raw_input('请输入文章标题: ')

    file_name = '_posts/{time}-{title}.md'.format(time=t, title=title.replace(' ', '-'))

    with open(file_name, 'w') as f:
        f.write(template)


if __name__ == '__main__':
    title = sys.argv[1] if len(sys.argv) > 1 else ''
    main(title)
