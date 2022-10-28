#!/usr/bin/python3
import os, urllib.request, shutil, zipfile, platform, stat

here = os.path.dirname(os.path.realpath(__file__))
here = here.replace('\\', '/')

url = 'http://mirrors.ustc.edu.cn/CTAN/indexing/zhmakeindex.zip'
file_name = here + '/downloads/zhmakeindex.zip'
if os.path.isfile(file_name) == False:
    if os.path.isdir(here + '/downloads') == False:
        os.mkdir(here + '/downloads')
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        print('正在下载 zhmakeindex, 请耐心等待...')
        shutil.copyfileobj(response, out_file)
print(r'zhmakeindex 已下载为 ' + file_name)

with zipfile.ZipFile(file_name, 'r') as f:
    f.extractall(path = here + '/external')

bit = platform.architecture()
system = platform.system()

if bit[0] == '64bit' and system == 'Linux':
    bin = here + '/external/zhmakeindex/bin/linux_x64/zhmakeindex'
    os.chmod(bin, stat.S_IRWXU)
elif bit[0] == '32bit' and system == 'Linux':
    bin = here + '/external/zhmakeindex/bin/linux_x86/zhmakeindex'
    os.chmod(bin, stat.S_IRWXU)
elif bit[0] == '64bit' and system == 'Windows':
    bin = here + '/external/zhmakeindex/bin/windows_x64/zhmakeindex.exe'
elif bit[0] == '32bit' and system == 'Windows':
    bin = here + '/external/zhmakeindex/bin/windows_x86/zhmakeindex.exe'

ist = here + '/external/zhmakeindex/examples/zh.ist'
zhmakeindex = r'\index_command "' + bin + r' -c -q -s ' + ist + '"\n'

if system == 'Linux': preferences = os.path.expanduser('~/.lyx/preferences')
elif system == 'Windows': preferences = os.path.expanduser(r'~\AppData\Roaming\LyX2.3\preferences') # 这里假设 LyX 2.3

if os.path.isfile(preferences):
    with open(preferences, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    index_command = True
    write_lines = []
    for line in lines:
        if line.startswith(r'\index_command'):
            index_command = False
            write_lines.append(r'#' + line)
            write_lines.append(zhmakeindex)
        else:
            write_lines.append(line)
    if index_command:
        write_lines.append(zhmakeindex)
else:
    write_lines = ['Format 24\n'] # 这里假设 LyX 2.3
    write_lines.append(zhmakeindex)
with open(preferences, 'w', encoding='utf-8') as f:
    f.writelines(write_lines)
