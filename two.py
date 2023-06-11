from screen import Screen
from screen import getScreenStr
from utils import run_cmd

# scale1 = getScreensScale(175, 100)
scale1 = 1.39

screen_left = Screen('HDMI-A-2', 1920, 1080, scale1)
screen_right = Screen('DisplayPort-2', 3840, 2160, 1.0)

total_x = screen_left.new_x + screen_right.new_x
total_y = max(screen_left.new_y, screen_right.new_y)

screen_right.pos_x = screen_left.new_x
screen_right.panning_x = screen_left.new_x

xrandr_command = 'xrandr --fb {}x{} \\'.format(total_x, total_y)

xrandr_command += '\n\t' + getScreenStr(screen_left) + " \\"
xrandr_command += '\n\t' + getScreenStr(screen_right)

print(xrandr_command)

# run_cmd(xrandr_command)
