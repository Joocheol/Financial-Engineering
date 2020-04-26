from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))

r = 1
up_node = 15
down_node = 10

class a20200426_1(Scene):
    def construct(self):
        
        grid = []
        for i in range(25):
            grid.append(Grid(1,1, height=0.5, width=0.5))
            grid[i].move_to([8*(i-25)/25+4, 3, 0]).scale(0.6)
            self.play(ShowCreation(grid[i]), run_time=0.1)
