class Screen(object):

    def __init__(self, name, x=1920, y=1080, scale=1.0, r='', off=False):
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

        self.r = r

        self.off = off

    def get_screen_str(self):
        if self.off:
            return '--output {} --off'.format(self.name)
        else:
            other_params = ''

            if len(self.r) > 0:
                other_params += ' -r {}'.format(self.r)

            return '--output {} --mode {}x{} --scale {}x{} --pos {}x{} --panning {}x{}+{}+{}'.format(
                self.name,
                self.x, self.y,
                self.scale, self.scale,
                self.pos_x, self.pos_y,
                self.new_x, self.new_y, self.panning_x, self.panning_y,
            ) + other_params
