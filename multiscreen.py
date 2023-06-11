from screen import Screen
from screen import getScreenStr

# screens = []
screens = [
    Screen('HDMI-A-2', 1920, 1080, 1.39),
    Screen('DisplayPort-2', 3840, 2160, 1.0)
]

if len(screens) == 0:
    exit(-1)

total_x = screens[0].new_x
total_y = screens[0].new_y

for i in range(1, len(screens)):
    total_x += screens[i].new_x
    total_y = max(total_y, screens[i].new_y)

    screens[i].pos_x = screens[i - 1].pos_x + screens[i - 1].new_x
    screens[i].panning_x = screens[i - 1].panning_x + screens[i - 1].new_x

xrandr_command = 'xrandr --fb {}x{}'.format(total_x, total_y)

for i in range(len(screens)):
    xrandr_command += ' \\\n\t' + getScreenStr(screens[i])

print(xrandr_command)


# run_cmd(xrandr_command)
