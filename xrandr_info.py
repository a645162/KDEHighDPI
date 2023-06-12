# -*- coding: utf-8 -*-

"""
@File       : xrandr_info.py
@Date       : 2023/6/12
@Author     : Haomin Kong
@Description: Extract useful information from the xrandr command execution results.
@IDE        : Pycharm
"""

import os

result = os.popen('xrandr')
res = result.read()

# print(res)

new_result = ""

r_list = res.split('\n')
list_len = len(r_list)
for i in range(list_len):
    if r_list[i].find(' connected ') != -1:
        if i + 1 < list_len and len(r_list[i + 1].strip()) > 0:
            new_result += r_list[i].strip() + '\n' + r_list[i + 1].strip() + "\n"

print(new_result)