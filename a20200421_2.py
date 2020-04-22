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

class a20200421_2(Scene):
    def construct(self):
        
        grid = []
        for i in range(25):
            grid.append(Grid(1,1, height=0.5, width=0.5))
            grid[i].move_to([8*(i-25)/25+4, 3, 0]).scale(0.6)
            self.play(ShowCreation(grid[i]), run_time=0.1)


        layer1 = []
        for i in range(up_node):
            layer1.append(Circle(radius=r))
            layer1[i].move_to([8*(i-up_node)/up_node+4, 0, 0]).scale(0.2).set_color(WHITE)
            self.play(ShowCreation(layer1[i]), run_time=0.1)

        lines = []
        for i in range(25):
            for j in range(up_node):
                s = grid[i].get_center()
                e = layer1[j].get_center()
                lines.append(Line(s, e).set_stroke(width=0.5))

        lines_g = VGroup(*lines)
        self.play(ShowCreation(lines_g))
           

        layer2 = []
        for i in range(down_node):
            layer2.append(Circle(radius=r))
            layer2[i].move_to([6*(i-down_node)/down_node+3, -3, 0]).scale(0.2).set_color(WHITE)
            self.play(ShowCreation(layer2[i]), run_time=0.1)

        lines = []
        for i in range(up_node):
            for j in range(down_node):
                s = layer1[i].get_center()
                e = layer2[j].get_center()
                lines.append(Line(s, e).set_stroke(width=0.5))

        lines_g = VGroup(*lines)
        self.play(ShowCreation(lines_g))