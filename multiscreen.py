# -*- coding: utf-8 -*-

"""
@File       : multiscreen.py
@Date       : 2023/6/11
@Author     : Haomin Kong
@Description: Calculate the command line used by xrandr
@IDE        : Pycharm
"""

from screen import Screen
from utils import run_cmd

Auto_Run = False

# 修改这里将自动执行命令！
# Modify here will automatically execute the command!

Auto_Run = True

# 修改这里!!!
# Modify here!!!
# 请从左到右依次填写
# Please fill in from left to right
screens = [
    Screen(name='HDMI-A-2', x=1920, y=1080, scale=1.6, r="143.99", off=False),
    Screen(name='DisplayPort-2', x=3840, y=2160, scale=1.0, off=False),
]

if len(screens) == 0:
    exit(-1)

total_x = screens[0].new_x
total_y = screens[0].new_y

for i in range(1, len(screens)):
    if screens[i].off:
        continue

    total_x += screens[i].new_x
    total_y = max(total_y, screens[i].new_y)

    last_valid_screen = -1
    for k in range(i - 1, -1, -1):
        if not screens[k].off:
            last_valid_screen = k
            break

    if last_valid_screen != -1:
        screens[i].pos_x = screens[last_valid_screen].pos_x + screens[last_valid_screen].new_x
        screens[i].panning_x = screens[last_valid_screen].panning_x + screens[last_valid_screen].new_x

xrandr_command = 'xrandr --fb {}x{}'.format(total_x, total_y)

for i in range(len(screens)):
    xrandr_command += ' \\\n\t' + screens[i].get_screen_str()

print(xrandr_command)

if Auto_Run:
    run_cmd(xrandr_command)
