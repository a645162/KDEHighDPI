class Screen(object):
    def __init__(self, name, x, y, scale=1.0):
        self.name = name

        self.x = x
        self.y = y

        self.scale = scale

        self.pos_x = 0
        self.pos_y = 0

        self.panning_x = 0
        self.panning_y = 0

        self.new_x = int(self.x * self.scale)
        self.new_y = int(self.y * self.scale)


def getScreenStr(screen):
    return '--output {} --mode {}x{} --scale {}x{} --pos {}x{} --panning {}x{}+{}+{}'.format(
        screen.name,
        screen.x, screen.y,
        screen.scale, screen.scale,
        screen.pos_x, screen.pos_y,
        screen.new_x, screen.new_y, screen.panning_x, screen.panning_y,
    )


screen_left = Screen('HDMI-A-2', 1920, 1080, 1.3)
screen_right = Screen('DisplayPort-2', 3840, 2160, 1)

total_x = screen_left.new_x + screen_right.new_x
total_y = max(screen_left.new_y, screen_right.new_y)

screen_right.pos_x = screen_left.new_x
screen_right.panning_x = screen_left.new_x

xrandr_command = 'xrandr --fb {}x{} \\'.format(total_x, total_y)

xrandr_command += '\n\t' + getScreenStr(screen_left) + " \\"
xrandr_command += '\n\t' + getScreenStr(screen_right)

print(xrandr_command)
