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

        # temp = []
        # node = [Circle(radius=0.3) for i in range(3)]
        # for i in range(3):
        #     node[i].move_to(LEFT*3+UP*(5-i))
        
        # temp = VGroup(*node, TextMobject("a"), *node)

        # brace1 = Brace(temp, LEFT, buff = SMALL_BUFF)

        # self.play(ShowCreation(temp))
        # self.play(ShowCreation(brace1))


        grid = Grid(10, 10, height=3, width=3)
        brace1 = Brace(grid, LEFT, buff=SMALL_BUFF)
        brace2 = Brace(grid, UP, buff=SMALL_BUFF)
        self.play(ShowCreation(grid))
        self.play(ShowCreation(brace1), ShowCreation(brace2))
        text1 = TextMobject("28")
        text2 = TextMobject("28")
        text1.next_to(brace1, LEFT)
        text2.next_to(brace2, UP)
        self.play(ShowCreation(text1), ShowCreation(text2))

        rect_UL = [Rectangle(height=1, width=1) for _ in range(5)]
        for i in range(5):
            rect_UL[i].move_to(UP*3+(LEFT*(5-i))+[-.3,0,0]).scale(0.5)
            self.play(Transform(grid.copy(), rect_UL[i]), run_time = 0.5)

        text3 = TexMobject("\\cdots")
        text3.move_to(UP*3)
        self.play(Write(text3))
        rect_UR = [Rectangle(height=1, width=1) for _ in range(5)]
        for i in range(5):
            rect_UR[i].move_to(UP*3+RIGHT*(i)+[1,0,0]).scale(0.5)
            self.play(Transform(grid.copy(), rect_UR[i]), run_time = 0.5)

        brace3 = Brace(VGroup(rect_UL[0], text3, rect_UR[4]), UP, buff=SMALL_BUFF)
        self.play(ShowCreation(brace3))

        text4 = TextMobject("6000")
        text4.next_to(brace3, UP)
        self.play(Write(text4))

