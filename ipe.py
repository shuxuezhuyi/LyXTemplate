
import sys, os
from pathlib import Path

if sys.version_info[0] != 3 :
    print('出错啦! 请使用 Python3 来执行脚本.')
    exit()

here = os.path.dirname(os.path.realpath(__file__))

p = Path(here) # 当前文件夹中所有 ipe 文档都会被处理
for ipe_path in list(p.glob('**/*.ipe')):
    ipe_file = str(ipe_path)
    pdf_file = ipe_file.replace('.ipe', '.pdf')
    if os.path.isfile(pdf_file) == False or os.path.getmtime(ipe_file) > os.path.getmtime(pdf_file):
        print('\n' + 'input: ' + ipe_file + '\n' + 'output: ' + pdf_file)
        os.system(r'tools\ipe\bin\iperender.exe' + ' -pdf "' + ipe_file + '" "' + pdf_file + '"')