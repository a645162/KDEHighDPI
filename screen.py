
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

        self.new_x = round(self.x * self.scale)
        self.new_y = round(self.y * self.scale)


def getScreenStr(screen):
    return '--output {} --mode {}x{} --scale {}x{} --pos {}x{} --panning {}x{}+{}+{}'.format(
        screen.name,
        screen.x, screen.y,
        screen.scale, screen.scale,
        screen.pos_x, screen.pos_y,
        screen.new_x, screen.new_y, screen.panning_x, screen.panning_y,
    )
