#!/usr/bin/python3
import os, configparser, re

here = os.path.dirname(os.path.realpath(__file__))
ini_path = os.path.dirname(here) + '/config.ini'
with open(ini_path, 'r', encoding='utf-8') as f:
    config = configparser.RawConfigParser()
    config.optionxform = lambda option: option
    config.read_file(f)

pre_preamble = here + '/pre_documents/pre_preamble.tex'
preamble = os.path.dirname(here) + '/preamble.tex'
with open(pre_preamble, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for item in config.items('PATH') + config.items('pre_preamble'):
    for i in range(len(lines)):
        lines[i] = re.sub(item[0], item[1], lines[i])
with open(preamble, 'w', encoding='utf-8') as f:
    f.writelines(lines)

pre_preamble_english = here + '/pre_documents/pre_preamble_english.tex'
preamble_english = os.path.dirname(here) + '/preamble_english.tex'
with open(pre_preamble_english, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for item in config.items('PATH') + config.items('pre_preamble'):
    for i in range(len(lines)):
        lines[i] = re.sub(item[0], item[1], lines[i])
with open(preamble_english, 'w', encoding='utf-8') as f:
    f.writelines(lines)
