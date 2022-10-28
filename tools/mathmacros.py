#!/usr/bin/python3
import os

here = os.path.dirname(os.path.realpath(__file__))
tex_path = os.path.dirname(here) + '/Other/MathMacros/MathMacros.tex'

with open(tex_path, 'r', encoding='utf-8') as tex_file:
    lines = tex_file.readlines()
with open(tex_path, 'w', encoding='utf-8') as tex_file:
    write_lines = []
    write_sign = False
    for line in lines:
        if not write_sign:
            if r'\begin{document}' in line: write_sign = True
            continue
        elif r'\end{document}' in line: break
        write_lines.append(line)
    tex_file.writelines(write_lines)
