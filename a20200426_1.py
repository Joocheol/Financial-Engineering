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

class Arrow_Debreu(Scene):
    def construct(self):

        text_010 = TextMobject("2. Arrow-Debreu Security")

        self.play(GrowFromCenter(text_010))
        self.wait(2)

        self.play(FadeOut(text_010))
        self.wait(1)

        game1 = TexMobject("10")
        game1.scale(0.7).move_to([-6,2,0])
        game1_up = TexMobject("11")
        game1_up.scale(0.7).move_to([-4,3,0])
        game1_down = TexMobject("11")
        game1_down.scale(0.7).move_to([-4,1,0])

        game2 = TexMobject("9")
        game2.scale(0.7).move_to([-1,2,0])
        game2_up = TexMobject("22")
        game2_up.scale(0.7).move_to([1,3,0])
        game2_down = TexMobject("0")
        game2_down.scale(0.7).move_to([1,1,0])

        game3 = TexMobject("?")
        game3.scale(0.7).move_to([4,2,0])
        game3_up = TexMobject("22")
        game3_up.scale(0.7).move_to([6,3,0])
        game3_down = TexMobject("11")
        game3_down.scale(0.7).move_to([6,1,0])

        self.play(
            Write(game1), Write(game1_up), Write(game1_down),
            Write(game2), Write(game2_up), Write(game2_down),
            Write(game3), Write(game3_up), Write(game3_down)
        )
        self.wait(1)

        text_020 = TextMobject("Now we want to price a new product.")
        text_020.to_edge(DOWN)

        self.play(Write(text_020))

        u1 = TextMobject("?")
        u1_up = TextMobject("1")
        u1_down = TextMobject("0")
        u1.move_to(LEFT+DOWN)
        u1_up.move_to(RIGHT)
        u1_down.move_to(RIGHT+DOWN*2)

        arrow1 = Arrow(u1.get_right(), u1_up.get_left(), buff=0.5)
        arrow2 = Arrow(u1.get_right(), u1_down.get_left(), buff=0.5)

        u1_all = VGroup(u1, u1_up, u1_down, arrow1, arrow2)
        self.play(
            Write(u1_all)
        )
        self.wait(1)

        text_030 = TextMobject("We know how to build the equations.")
        text_030.to_edge(DOWN)

        self.play(FadeOut(text_020))
        self.play(Write(text_030))

        formula_010 = TexMobject(r"""
            \begin{bmatrix} 11 \\ 11 \end{bmatrix}
            \times x_1 +
            \begin{bmatrix} 22 \\ 0 \end{bmatrix}
            \times x_2
            =
            \begin{bmatrix} 1 \\ 0 \end{bmatrix}        
        """)
        formula_010.move_to(DOWN)

        self.play(ReplacementTransform(u1_all, formula_010))

        text_040 = TextMobject("By solving the equations, we get")
        text_040.to_edge(DOWN)

        self.play(FadeOut(text_030))
        self.play(Write(text_040))

        formula_020 = TexMobject(r"""
            x_1 = 0, \quad x_2 = {1 \over 22}         
        """)
        formula_020.move_to(DOWN)

        self.play(ReplacementTransform(formula_010, formula_020))

        text_050 = TextMobject("So the price of the new product is $9 \\over 22$.")
        text_050.to_edge(DOWN)

        self.play(FadeOut(text_040))
        self.play(Write(text_050))

        formula_030 = TexMobject(r"""
            10 \times 0 + 9 \times {1 \over 22} = {9 \over 22}         
        """)
        formula_030.move_to(DOWN)

        self.play(ReplacementTransform(formula_020, formula_030))
        self.play(FadeOut(formula_030))
        self.play(FadeOut(text_050))
        
############
 
        text_060 = TextMobject("Another try for another new product.")
        text_060.to_edge(DOWN)

        self.play(Write(text_060))

        u2 = TextMobject("?")
        u2_up = TextMobject("0")
        u2_down = TextMobject("1")
        u2.move_to(LEFT+DOWN)
        u2_up.move_to(RIGHT)
        u2_down.move_to(RIGHT+DOWN*2)

        arrow1 = Arrow(u2.get_right(), u2_up.get_left(), buff=0.5)
        arrow2 = Arrow(u2.get_right(), u2_down.get_left(), buff=0.5)

        u2_all = VGroup(u2, u2_up, u2_down, arrow1, arrow2)
        self.play(
            Write(u2_all)
        )
        self.wait(1)

        text_070 = TextMobject("Similar, but different equations.")
        text_070.to_edge(DOWN)

        self.play(FadeOut(text_060))
        self.play(Write(text_070))

        formula_040 = TexMobject(r"""
            \begin{bmatrix} 11 \\ 11 \end{bmatrix}
            \times x_1 +
            \begin{bmatrix} 22 \\ 0 \end{bmatrix}
            \times x_2
            =
            \begin{bmatrix} 0 \\ 1 \end{bmatrix}        
        """)
        formula_040.move_to(DOWN)

        self.play(ReplacementTransform(u2_all, formula_040))

        text_080 = TextMobject("By solving the equations, we get")
        text_080.to_edge(DOWN)

        self.play(FadeOut(text_070))
        self.play(Write(text_080))

        formula_050 = TexMobject(r"""
            x_1 = {1 \over 11}, \quad x_2 = -{1 \over 22}        
        """)
        formula_050.move_to(DOWN)

        self.play(ReplacementTransform(formula_040, formula_050))

        text_090 = TextMobject("So the price of the new product is ${11 \\over 22}$.")
        text_090.to_edge(DOWN)

        self.play(FadeOut(text_080))
        self.play(Write(text_090))

        formula_060 = TexMobject(r"""
            10 \times {1 \over 11} + 9 \times -{1 \over 22} = {11 \over 22}         
        """)
        formula_060.move_to(DOWN)

        self.play(ReplacementTransform(formula_050, formula_060))
        self.play(FadeOut(formula_060))
        self.play(FadeOut(text_090))
