# 需要用 Python3 执行

import sys, os, shutil, subprocess
from pathlib import Path

if sys.version_info[0] != 3 :
    print('出错啦! 请使用 Python3 来执行脚本.')
    exit()

here = os.path.dirname(os.path.realpath(__file__))

os.system('python -tt ' + '"' + here + '/tools/pre_config.py"')
print(r'已生成 config.ini.')

depend = here + '/.depend/lyx/layouts'
layouts = os.path.expanduser(r'~\AppData\Roaming\LyX2.3\layouts') # 这里假设 LyX 2.3
for file in os.listdir(depend):
    shutil.copy(depend + '/' + file , layouts)
print('已复制 layout 文件.')

try: 
    LyX = os.path.dirname(subprocess.check_output('where lyx').decode().splitlines()[0])
except subprocess.CalledProcessError:
    LyX = os.path.expanduser(r'~\AppData\Local\LyX 2.3\bin')
if os.path.isfile(LyX + r'\lyx.exe') == False: LyX = r'C:\Program Files\LyX 2.3\bin'
while os.path.isfile(LyX + r'\lyx.exe') == False:
    print('在 ' + LyX + ' 中找不到 lyx.exe !')
    LyX = input(r'请输入 lyx.exe 所在的文件夹(例如 D:\program\LyX\bin ), 按回车结束.' + '\n')
print('lyx.exe 在 ' + LyX + ' 中.')

os.chdir(os.path.expanduser(r'~\AppData\Roaming\LyX2.3')) # 这里假设 LyX 2.3
python2 = '"' + os.path.dirname(LyX) + r'\Python\python.exe"'
subprocess.run(python2 + ' -tt "' + os.path.dirname(LyX) + r'\Resources\configure.py"' + ' --binary-dir="' + LyX + r'\"', check = True)
os.chdir(here)
print(r'已重配置 LyX.')

subprocess.run('python -tt ' + '"' + here + '/tools/zhmakeindex.py"', check = True)
print(r'已配置 zhmakeindex.')

subprocess.run('python -tt ' + '"' + here + '/tools/pre_preamble.py"', check = True)
print(r'已生成 preamble.tex 与 preamble_english.tex.')

mathmacros = '"' + here + '/Other/MathMacros/MathMacros.lyx"'
mathmacros = mathmacros.replace('/', '\\')
subprocess.run(LyX + r'\lyx.exe -e xetex ' + mathmacros, check = True)
subprocess.run('python -tt ' + '"' + here + '/tools/mathmacros.py"', check = True)
print(r'已生成 MathMacros.tex.')

# 安装 ipe-7.2.26
subprocess.run('python -tt ' + '"' + here + '/tools/install_ipe.py"', check = True)

# 把本项目中所有 ipe 文档都转换为对应的 pdf 文档
subprocess.run('python -tt ' + '"' + here + '/ipe.py"', check = True)

print(r'正在生成 LearningMath.pdf, 可能需要几分钟, 请耐心等待...')
LearningMath = here + '/LearningMath.lyx'
LearningMath = LearningMath.replace('/', '\\')
subprocess.run(LyX + r'\lyx.exe -e pdf4 "' + LearningMath + '"', check = True)
print(r'已生成 LearningMath.pdf.')

print('执行完毕.')