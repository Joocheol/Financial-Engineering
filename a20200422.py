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

class a20200422(Scene):
    def construct(self):
        
        grid = []
        for i in range(25):
            grid.append(Grid(1,1, height=0.5, width=0.5))
            grid[i].move_to([8*(i-25)/25+4, 3, 0]).scale(0.6)
            self.play(ShowCreation(grid[i].set_color(BLUE)), run_time=0.1)


        layer1 = []
        for i in range(up_node):
            layer1.append(Circle(radius=r))
            layer1[i].move_to([8*(i-up_node)/up_node+4, 0, 0]).scale(0.2).set_color(BLACK)
            if i == 0:
                layer1[i].set_color(YELLOW)
            #self.play(ShowCreation(layer1[i]), run_time=0.1)
            self.add(layer1[i])

        lines = []
        for i in range(25):
            for j in range(up_node):
                s = grid[i].get_center()
                e = layer1[j].get_center()
                if j == 0:
                    lines.append(Line(s, e).set_stroke(width=0.5).set_color(WHITE))
                else:
                    lines.append(Line(s, e).set_stroke(width=0.5).set_color(BLACK))
                
        lines_g = VGroup(*lines)
        self.play(ShowCreation(lines_g))

        formula1 = Tex(
            "&f_", "{1}",
            "(", "x_", "{1}", ", x_", "{2}", ", \\cdots ", "x_", "{784}",
            ") \\\\", 
            "= &", "w_", "{1", ",", "1}", " x_", "{1}",
            "+", "w_", "{1", ",", "2}", " x_", "{2}",
            "+","\\cdots",
            "+", "w_", "{1", ",", "784}", " x_", "{784}",
            "+", "b_", "{1}")

        [formula1[i].set_color(YELLOW) for i in (1,13,20,29,36)]
        [formula1[i].set_color(BLUE) for i in (4,6,9,15,17,22,24,31,33)]

        self.play(Write(formula1.move_to(RIGHT+DOWN)))
        self.wait()

        formula2 = Tex(
            "\\begin{bmatrix} W \\end{bmatrix}_{128 \\times 784}",
            "\\begin{bmatrix} x \\end{bmatrix}_{784 \\times 1}",
            "+ \\begin{bmatrix} b \\end{bmatrix}_{128 \\times 1}")

        self.play(Write(formula2.move_to(RIGHT+DOWN*3)))
           

        # layer2 = []
        # for i in range(down_node):
        #     layer2.append(Circle(radius=r))
        #     layer2[i].move_to([6*(i-down_node)/down_node+3, -3, 0]).scale(0.2).set_color(WHITE)
        #     self.play(ShowCreation(layer2[i]), run_time=0.1)

        # lines = []
        # for i in range(up_node):
        #     for j in range(down_node):
        #         s = layer1[i].get_center()
        #         e = layer2[j].get_center()
        #         lines.append(Line(s, e).set_stroke(width=0.5))

        # lines_g = VGroup(*lines)
        # self.play(ShowCreation(lines_g))