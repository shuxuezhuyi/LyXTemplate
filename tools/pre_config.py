#!/usr/bin/python3
import os, re

here = os.path.dirname(os.path.realpath(__file__))
here = here.replace('\\', '/')
ini_path = os.path.dirname(here) + '/config.ini'

pre_preamble = """

[pre_preamble]
MATHIST_MAIN_FONT = 宋体
MATHIST_BOLD_FONT = 黑体
MATHIST_ITALIC_FONT = 楷体
MATHIST_SANS_FONT = 宋体
MATHIST_MONO_FONT = 宋体
MATHIST_THEOREM_MAIN_FONT = 宋体
MATHIST_THEOREM_BOLD_FONT = 黑体
MATHIST_THEOREM_ITALIC_FONT = 楷体

"""

if os.path.isfile(ini_path) == False:
    lines = []
    lines.append('[PATH]\n')
    lines.append('MATHIST_DOCUMENT_PATH = ' + os.path.dirname(here) + '\n')
    lines.append(pre_preamble)
    with open(ini_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)