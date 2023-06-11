import os
import pathlib
import re

mission = {'HDMI': '1'}

path = str(pathlib.Path.home()) + r'/.config/kdeglobals'

if not os.path.exists(path):
    exit(1)

f = open(path, 'r')
code = f.read().strip()
f.close()

if len(code) == 0:
    exit(2)

regex_KScreen = re.compile(r'\[KScreen]\nScaleFactor=.*\nScreenScaleFactors=.*\n')

result = re.findall(regex_KScreen, code)

if len(result) != 1:
    exit(3)
else:
    print(result[0].strip())
    ori_code = result[0].strip()
    result = ori_code.split('\n')

# print(result)
if len(result) != 3:
    exit(4)

if result[1].strip().find('ScaleFactor=') != 0:
    exit(5)
result[1] = result[1].strip()[len('ScaleFactor='):]

if result[2].strip().find('ScreenScaleFactors=') != 0:
    exit(6)
result[2] = result[2].strip()[len('ScreenScaleFactors='):]

result = result[1:]

# print(result)

key_list = mission.keys()

port_list = str(result[1]).split(';')
for i in range(len(port_list)):
    port_list[i] = port_list[i].strip()

    for k in key_list:
        if port_list[i].upper().find(k.upper()) != -1:
            item = port_list[i].split('=')
            if len(item) != 2:
                exit(7)
            item[1] = mission[k]
            port_list[i] = item[0] + '=' + item[1]

new_port = ''
for port in port_list:
    if len(port) == 0:
        continue
    new_port += port + ";"

# print(new_port)]

result[0] = '1'

new_str = """
[KScreen]
ScaleFactor={}
ScreenScaleFactors={}
""".format(result[0], new_port).strip()

print()
print(new_str)
