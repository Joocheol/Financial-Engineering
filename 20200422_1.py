from manimlib.imports import *

r = 1
up_node = 15
down_node = 10

class a20200422_1(Scene):
    def construct(self):

        # grid = Grid(1,10)
        # self.play(ShowCreation(grid))

        text = TexMobject("\\begin{bmatrix}" "f_a = x^2" "\\end{bmatrix")
        # text.set_color_by_tex_to_color_map({"f" : RED})
        # self.play(Write(text[0]))

        matrix = Matrix([["f_a", "\\cdots", 1], ["a", "...", "c^2"]])
        matrix[0][3].set_color(RED)
        self.play(ShowCreation(matrix))
        self.wait()

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

