# -*- coding: utf-8 -*-

"""
@File       : x11.py
@Date       : 2023/6/14
@Author     : Haomin Kong
@Description: Calculate the command line used by xrandr
@IDE        : Pycharm
"""

import time

from screen import Screen
from utils import run_cmd

# Auto_Run = False
Auto_Run = True
# 修改这里将自动执行命令！
# Modify here will automatically execute the command!


# 修改这里!!!
# Modify here!!!
# 请从左到右依次填写
# Please fill in from left to right
screens = [
    Screen(name='DisplayPort-1', x=3840, y=2160, scale=1.0, off=False),
    Screen(name='DisplayPort-2', x=1920, y=1080, scale=1.6, r="143.99", off=False),
    Screen(name='DVI-D-1-0', off=True),
]


def generate_command(screen_list, auto_run):
    total_screen_count = len(screen_list)

    if total_screen_count == 0:
        exit(-1)

    first_screen_index = -1

    for i in range(0, total_screen_count):
        if not screen_list[i].off:
            first_screen_index = i
            break

    if first_screen_index == -1:
        print("No screen!")
        exit(1)

    total_x = screen_list[first_screen_index].new_x
    total_y = screen_list[first_screen_index].new_y

    for i in range(first_screen_index + 1, total_screen_count):
        if screen_list[i].off:
            continue

        total_x += screen_list[i].new_x
        total_y = max(total_y, screen_list[i].new_y)

        last_valid_screen = -1
        for k in range(i - 1, -1, -1):
            if not screen_list[k].off:
                last_valid_screen = k
                break

        if last_valid_screen != -1:
            screen_list[i].pos_x = screen_list[last_valid_screen].pos_x + screen_list[last_valid_screen].new_x
            screen_list[i].panning_x = screen_list[last_valid_screen].panning_x + screen_list[last_valid_screen].new_x

    xrandr_command = 'xrandr --fb {}x{}'.format(total_x, total_y)

    for i in range(len(screen_list)):
        xrandr_command += ' \\\n\t' + screen_list[i].get_screen_str()

    print(xrandr_command)

    if auto_run:
        run_cmd(xrandr_command)


screens1 = []
change = False

for screen in screens:
    if not screen.off and screen.scale != 1.0:
        change = True
        screens1.append(Screen(name=screen.name, off=True))
    else:
        screens1.append(screen)

if change:
    generate_command(screens1, Auto_Run)
    time.sleep(2)
    print()

generate_command(screens, Auto_Run)
