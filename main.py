class Screen(object):
    def __init__(self,name, x, y, scale=1.0):
        self.name = name

        self.x = x
        self.y = y

        self.scale = scale


screen_left = Screen('HDMI-A-2',1920, 1080, 1.3)
screen_right = Screen('DisplayPort-2',3840, 2160, 1)

total_x = screen_left.x * screen_left.scale + screen_right.x * screen_right.scale
total_y = max(screen_left.y * screen_left.scale , screen_right.y * screen_right.scale)



