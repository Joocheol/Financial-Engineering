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

class a20200421(Scene):
    def construct(self):

        num = 5
        grid = [Grid(1, 5, height=0.5, width=2.5) for _ in range(num)]
        for i in range(num):
            grid[i].move_to([0, i*0.5, 0])
        grid_g = VGroup(*grid)

        self.play(FadeIn(grid_g))

        grid1 = [Grid(1, 5, height=0.5, width=2.5) for _ in range(num)]
        for i in range(num):
            grid[i].move_to([i*2.5-5, -1, 0]).set_color(GRAY)
            self.play(Transform(grid1[i], grid[i]))
            grid1[i].set_color(WHITE)
            self.play(ShowCreation(grid1[i]))
            
        

        
