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

        image1 = ImageMobject("mnist.png")
        image2 = ImageMobject("mnist.png")
        image2.move_to(LEFT*4)
        self.play(FadeIn(image1))
        self.play(Transform(image1, image2))

        # temp = []
        # node = [Circle(radius=0.3) for i in range(3)]
        # for i in range(3):
        #     node[i].move_to(LEFT*3+UP*(5-i))
        
        # temp = VGroup(*node, TextMobject("a"), *node)

        # brace1 = Brace(temp, LEFT, buff = SMALL_BUFF)

        # self.play(ShowCreation(temp))
        # self.play(ShowCreation(brace1))


        grid = Grid(14, 14, height=2, width=2)
        grid.move_to(LEFT*4)
        brace1 = Brace(grid, RIGHT, buff=SMALL_BUFF)
        brace2 = Brace(grid, UP, buff=SMALL_BUFF)
        self.play(ShowCreation(grid))
        self.play(ShowCreation(brace1), ShowCreation(brace2))
        text1 = TextMobject("28")
        text2 = TextMobject("28")
        text1.next_to(brace1, RIGHT)
        text2.next_to(brace2, UP)
        self.play(ShowCreation(text1), ShowCreation(text2))

        rect_UP = [Rectangle(height=1, width=1) for _ in range(3)]
        for i in range(3):
            rect_UP[i].move_to(UP*(3-i)+LEFT*0).scale(0.7)
            self.play(Transform(grid.copy(), rect_UP[i]), run_time = 0.5)

        text3 = Tex("\\vdots")
        text3.move_to(LEFT*0)
        self.play(Write(text3))
        rect_DOWN = [Rectangle(height=1, width=1) for _ in range(3)]
        for i in range(3):
            rect_DOWN[i].move_to(DOWN*(i+1)+LEFT*0).scale(0.7)
            self.play(Transform(grid.copy(), rect_DOWN[i]), run_time = 0.5)

        brace3 = Brace(VGroup(rect_UP[0], text3, rect_DOWN[2]), RIGHT, buff=SMALL_BUFF)
        self.play(ShowCreation(brace3))

        text4 = TextMobject("60,000")
        text4_1 = TextMobject("training")
        text4.next_to(brace3, RIGHT)
        text4_1.next_to(text4, DOWN)
        self.play(Write(text4), Write(text4_1))

        rect_UP = [Rectangle(height=1, width=1) for _ in range(3)]
        for i in range(3):
            rect_UP[i].move_to(UP*(3-i)+RIGHT*3.5).scale(0.7)
            self.play(Transform(grid.copy(), rect_UP[i]), run_time = 0.5)

        text3 = Tex("\\vdots")
        text3.move_to(RIGHT*3.5)
        self.play(Write(text3))
        rect_DOWN = [Rectangle(height=1, width=1) for _ in range(3)]
        for i in range(3):
            rect_DOWN[i].move_to(DOWN*(i+1)+RIGHT*3.5).scale(0.7)
            self.play(Transform(grid.copy(), rect_DOWN[i]), run_time = 0.5)

        brace3 = Brace(VGroup(rect_UP[0], text3, rect_DOWN[2]), RIGHT, buff=SMALL_BUFF)
        self.play(ShowCreation(brace3))

        text4 = TextMobject("10,000")
        text4_1 = TextMobject("testing")
        text4.next_to(brace3, RIGHT)
        text4_1.next_to(text4, DOWN+RIGHT*0)
        self.play(Write(text4), Write(text4_1))