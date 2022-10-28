#!/usr/bin/python3

from pathlib import Path
import re, os

here = os.path.dirname(os.path.realpath(__file__))

# 读取 template
# 注意: template_english 由 template 修改而成, 并未使用 template_english.lyx

template_path = os.path.dirname(here) + '/template/template/template.lyx'

with open(template_path,'r',encoding='utf-8') as read_file:
	template_data = read_file.readlines()
read_file.closed

# 截取开头的文本

template_lines = []
for line in template_data:
    if r'\begin_body' in line: break
    template_lines.append(line)

# 定义修改文件的函数
def change_file(read_file_path, write_file_path):
    """修改文件头"""
    
    with open(read_file_path,'r',encoding='utf-8') as read_file:
	    read_data = read_file.readlines()

    # 有些行要用原来的
    preamble = '\\input{../../preamble}\n'
    master = ''
    language = '\\language chinese-simplified\n'
    spacing = '\\spacing other 1.23\n'
    for line in read_data:
        if r'\begin_body' in line: break
        if r'\input{' in line: preamble = line
        elif r'\master ' in line: master = line
        elif r'\language ' in line: language = line
        elif r'\spacing ' in line: spacing = line

    # 准备要写入的文件头
    write_lines = []
    for line in template_lines:
        if r'\input{' in line: line = preamble
        elif r'\master ' in line: line = master
        elif r'\language ' in line: line = language
        elif r'\spacing ' in line: line = spacing
        write_lines.append(line)

    write_sign = False
    for line in read_data:
        if not write_sign:
            if r'\begin_body' in line:
                write_sign = True
                write_lines.append(line)
            continue
        write_lines.append(line)

    with open(write_file_path,'w',encoding='utf-8') as write_file:
        write_file.writelines(write_lines)

# 读取文件列表

p = Path(os.path.dirname(here)) # 在这个文件夹里面的所有 lyx 文档都会被处理

# 循环

for lyx_path in list(p.glob('**/*.lyx')):
    str_path = str(lyx_path)
    if os.path.dirname(here) + r'/temp/' in str_path: continue
    if os.path.dirname(here) + r'/template/' in str_path: continue
    change_file(str_path.replace('LearningMath/','LearningMath_b/'), str_path)
