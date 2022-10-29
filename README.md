## 我用 LyX 撰写数学笔记的模板

### 本项目使用的工具

主要用 LyX 2.3.6.1; 项目地址是 http://www.lyx.org/ . 建议使用 2.3.x 的最新版本. 你可以在 https://mirrors6.tuna.tsinghua.edu.cn/lyx/bin/ 里面找到历代 LyX 的安装包, 例如 LyX 2.3.6.1 的64位安装包是 https://mirrors6.tuna.tsinghua.edu.cn/lyx/bin/2.3.6/LyX-2361-Installer-3-x64.exe . 注意: 清华大学开源镜像站同时支持 ipv4 与 ipv6, 但本文提供的链接只写了 ipv6 的版本; 如果你的网络不支持 ipv6, 请把链接中的 mirrors6 改成 mirrors.

绘图用 Ipe 7.2.26; 项目地址是 http://ipe.otfried.org/ . 建议使用 7.2.x 的最新版本. 本项目的Windows安装脚本 tools/install_ipe.py 会从 GitHub 下载 Ipe 并解压到 tools/ipe 中, 里面的 bin/ipe.exe 就是 Ipe 主程序, 可以用它来编辑 ipe 文档.

使用 TeXLive 2022 生成 pdf 文档; 项目地址是 https://tug.org/texlive/ . 建议使用最新版. 你可以从 https://mirrors6.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/texlive.iso 下载到安装镜像.

使用 zhmakeindex 1.2 生成中文索引; 项目地址是 https://github.com/leo-liu/zhmakeindex . 建议使用最新版. 本项目的安装脚本 tools/zhmakeindex.py 会从中科大开源镜像站下载 zhmakeindex 并解压到 tools/zhmakeindex 中.

使用 Biber 2.16 与 Biblatex 3.16 生成参考文献; 项目地址是 https://github.com/plk/biber . 它们都包含在 TeXLive 中.

使用 showlabels 宏包以显示交叉引用的标签名; 你可以在 preamble.tex 中删除它.

### 如何编译

#### 注意事项

无论是哪一种编译方式, 都会修改你的 LyX 的配置. 具体有:

1. 生成索引的命令将被修改为调用 zhmakeindex.

2. 本项目的 .depend/lyx/layouts 中的 layout 文件都会被添加到你的用户目录中. 其中 stdclass.inc 和 patch-mathist.inc 很可能会改变你的 LyX 的样子, 但它们并非必要, 对于编译更是没有任何影响, 你可以删掉它们.

#### 在 Linux 中编译

在 Debian 11 中, 确保已完整安装 texlive, lyx, ipe 与 fonts-cmu, 并且确保已安装宋体、黑体与楷体这三种字体; 然后依次执行 `make install` 与 `make`. 这个过程将会重新配置 LyX, 请确保 LyX 没有在运行.

#### 在 Windows 中编译

1. 确保已安装 python3 (记得勾选"Add Python 3.x to PATH"), texlive, lyx. 注意: texlive 务必完整安装, 并在安装 lyx 之前安装. 请确保 latex.exe 所在路径已经被加到 PATH 中; 要确认这一点, 请在 cmd 里运行 `latex --version`, 期待的输出是以 pdfTeX 开头的几行字.

如果你曾经安装 python, 请确保本次编译时命令行的 python 命令指向 python3. 要确认这一点, 请在 cmd 里运行 `python --version`; 期待的输出是 `Python 3.x.x`, 例如 `Python 3.10.2`. 如果 PATH 之前没设置对, 请手动改过来. 在文件浏览器的地址栏中输入
`控制面板\用户帐户\用户帐户`
按回车键后, 左侧有个入口是`更改我的环境变量`, 点进去之后修改即可.

2. 然后在 LyX 已经关闭的情况下双击运行脚本 install_win.bat.

![install.svg](/picture/install_win.svg)

3. 目前以下脚本都假定 LyX 的版本号是 2.3, 如果你要用其它版本的 LyX 编译, 请手动修改它们: install_win.py 和 tools/zhmakeindex.py .

4. install_win.py 是按照仅运行一次的要求编写的, 平时请不要用它来编译. 平时请用脚本 ipe.bat (双击运行) 把 ipe 文档转换为 pdf 文档, 然后用 LyX 打开主文档 LearningMath.lyx, 使用 **XeTeX** 方式导出对应的 pdf 文档.

### 如何使用

#### 增加新的一章(chapter)

建议笔记的每一部分(part)占一个文件夹, 而每一章又在里面占一个文件夹. 如下图所示:

![part-chapter.svg](/picture/part-chapter.svg)

注意: 文件夹和文件最好不要用中文名, 否则程序可能出错. 上图用中文只是为了方便理解而已.

在创建了 新章.lyx 之后, 打开 LearningMath.lyx, 在需要插入的位置点击左键, 然后从菜单依次选中 插入→文件→子文档→浏览, 找到并选择 新章.lyx, 最后确认即可.

#### 用 Ipe 创建与编辑图片

Ipe 文档后缀名为 .ipe. 在 Windows 中, 要创建 ipe 文档, 请运行项目文件夹中的 tools→ipe→bin→ipe.exe. 要编辑已有的 ipe 文档, 也是用这个 ipe.exe, 只要右键点击 ipe 文档, 选择 打开方式→选择其他应用→更多应用→在这台电脑上查找其他应用, 找到上述 ipe.exe 即可, 勾选“始终使用此应用打开 .ipe 文件”之后就可以双击 ipe 文档来编辑了.

#### 插入 Ipe 创建的图片

ipe 文档不能直接插入 lyx 文档中. 先双击运行 ipe.bat 把新建或新近修改的 ipe 文档转换成 pdf 文件, 再把 pdf 文件当作图片插入到 lyx 文档中.

#### 添加自定义数学宏

打开 Other→MathMacros→MathMacros.lyx, 模仿着添加, 语法形如“宏的名字 := 宏的定义 宏在LyX中的显示效果”. 添加之后保存 MathMacros.lyx, 然后双击运行 mathmacros.bat 以生成新的 MathMacros.tex.

#### 添加与修改参考文献

先以 Biblatex 的格式编辑 reference.bib. 建议使用 JabRef 编辑, 其官网是 https://www.jabref.org/ . 编辑并保存 reference.bib 之后, 正在编辑 LearningMath.lyx 或其子文档的 LyX 会检测到 reference.bib 的变动, 然后你就可以在 lyx 文档中插入新的文献引用了.

#### 配合 Git

注意检查 .gitignore 的内容, 有些文件需要强制暂存才能提交到 git 仓库. 可以修改 .gitignore 以满足你自己的需求.

#### LyX 的具体用法可能不是本文的内容, 而是 LyX 的帮助文档的内容.

### Q&A

Q: 为什么用 LyX, 而不是用 TeXStudio 敲 TeX 源代码?

A: 因为本项目是 LyX 模板. 另外, 虽然 LyX 有自己的文档格式, 但它总是可以导出 tex 格式的文档.

Q: 已经有 [The Stacks project](https://stacks.math.columbia.edu/) 了, 何必自己写数学笔记?

A: The Stacks project 是一个伟大的项目, 但它不是中文的.

Q: 已经有维基百科了, 何必自己写数学笔记?

A: 我无法浏览维基百科. 再说维基百科也没有消灭 The Stacks project.

Q: 笔记还是手写最方便! 为什么要用电脑敲?

A: 因为我写字又慢又丑. 另外, 电子文档方便分享.

Q: 我不想搞那么多个文件. 可以把所有笔记都写进一个 lyx 文档吗?

A: 可以.