from manimlib.imports import *

class Arbitrage(Scene):
    def construct(self):

        text_010 = TextMobject("Arbitrage")

        self.play(GrowFromCenter(text_010))
        self.wait(2)

        self.play(FadeOut(text_010))
        self.wait(1)

        game1 = Tex("10")
        game1.scale(1).move_to(LEFT*4+UP*2)
        game1_up = Tex("11")
        game1_up.scale(1).move_to(LEFT*3+UP*3)
        game1_down = Tex("11")
        game1_down.scale(1).move_to(LEFT*3+UP*1)

        game2 = Tex("9")
        game2.scale(1).move_to(LEFT+UP*2)
        game2_up = Tex("22")
        game2_up.scale(1).move_to(RIGHT*0+UP*3)
        game2_down = Tex("0")
        game2_down.scale(1).move_to(RIGHT*0+UP*1)

        game3 = Tex("14.5")
        game3.scale(1).move_to(RIGHT*2+UP*2)
        game3_up = Tex("22")
        game3_up.scale(1).move_to(RIGHT*3+UP*3)
        game3_down = Tex("11")
        game3_down.scale(1).move_to(RIGHT*3+UP*1)

        self.play(
            Write(game1), Write(game1_up), Write(game1_down),
            Write(game2), Write(game2_up), Write(game2_down),
            Write(game3), Write(game3_up), Write(game3_down)
        )
        self.wait(1)

        text_020 = TextMobject("Let me explain the self-financing portfolio.")
        text_020.to_edge(DOWN)

        self.play(Write(text_020))
        self.play(FadeOut(text_020))

        text_030 = TextMobject("Suppose that I want to have  $[1, 0.5, -1]$ portfolio.")
        text_030.to_edge(DOWN)

        formula = Tex(r"""
            [1, 0.5, -1]
        """)
        formula.move_to(DOWN)

        self.play(ShowCreation(formula))

        self.play(Write(text_030))
        self.play(FadeOut(text_030))

        text_040 = TextMobject("The cost of building $[1, 0.5, -1]$ portfolio is 0.")
        text_040.to_edge(DOWN)

        formula_010 = Tex(r"""
            10 \times 1 + 9 \times 0.5 + 14.5 \times (-1) = 0
        """)
        formula_010.move_to(DOWN)

        self.play(Transform(formula, formula_010))

        self.play(Write(text_040))
        self.play(FadeOut(text_040))

        text_050 = TextMobject("Since it costs nothing, we call it as \"self-financing\".")
        text_050.to_edge(DOWN)

        self.play(Write(text_050))
        self.play(FadeOut(text_050))

        text_060 = TextMobject("Now calculate the future payoff of this portfolio.")
        text_060.to_edge(DOWN)

        formula_010 = Tex(r"""
            \begin{bmatrix} 11 \\ 11 \end{bmatrix} 
            \times 1 + 
            \begin{bmatrix} 22 \\ 0 \end{bmatrix} 
            \times 0.5 + 
            \begin{bmatrix} 22 \\ 11 \end{bmatrix} 
            \times (-1) = 
            \begin{bmatrix} 0 \\ 0 \end{bmatrix} 
        """)
        formula_010.move_to(DOWN)

        self.play(Transform(formula, formula_010))

        self.play(Write(text_060))
        self.play(FadeOut(text_060))

        text_070 = TextMobject("Since we begin with nothing, it is natual to end with nothing.")
        text_070.to_edge(DOWN)

        self.play(Write(text_070))
        self.play(FadeOut(text_070))

        text_080 = TextMobject("However, if something is out of equilibrium,")
        text_080.to_edge(DOWN)

############
        temp = TextMobject("15")
        temp.scale(1).move_to(RIGHT*2+UP*2)
        temp.set_color(RED)

        framebox1 = SurroundingRectangle(temp, buff = .1)
        self.play(ReplacementTransform(game3, temp))
        self.play(ShowCreation(framebox1))
#############

        self.play(FadeOut(formula))
        self.play(Write(text_080))
        self.play(FadeOut(text_080))

        text = TextMobject("we can take advantage of it, so called \"arbitrage\"")
        text.to_edge(DOWN)

        self.play(Write(text))
        self.play(FadeOut(text))


        text = TextMobject("Let\'s take the previous [1, 0.5, -1] postions.")
        text.to_edge(DOWN)

        formula_010 = Tex(r"""
            10 \times 1 + 9 \times 0.5 + 15 \times (-1) = -0.5
        """)
        formula_010.move_to(DOWN)

        self.play(Transform(formula, formula_010))

        self.play(Write(text))
        self.play(FadeOut(text))

        text = TextMobject("This time, the current cost is not 0, it is -0.5")
        text.to_edge(DOWN)

        self.play(Write(text))
        self.play(FadeOut(text))

        text = TextMobject("The cost is -0.5! Actually that's the money in your pocket.")
        text.to_edge(DOWN)

        self.play(Write(text))
        self.play(FadeOut(text))

        text_060 = TextMobject("Now calculate the future payoff of this portfolio.")
        text_060.to_edge(DOWN)

        formula_010 = Tex(r"""
            \begin{bmatrix} 11 \\ 11 \end{bmatrix} 
            \times 1 + 
            \begin{bmatrix} 22 \\ 0 \end{bmatrix} 
            \times 0.5 + 
            \begin{bmatrix} 22 \\ 11 \end{bmatrix} 
            \times (-1) = 
            \begin{bmatrix} 0 \\ 0 \end{bmatrix} 
        """)
        formula_010.move_to(DOWN)

        self.play(Transform(formula, formula_010))

        self.play(Write(text_060))
        self.play(FadeOut(text_060))

        text_070 = TextMobject("We begin with money in the pocket, and it ends with all 0\'s")
        text_070.to_edge(DOWN)

        self.play(Write(text_070))
        self.play(FadeOut(text_070))

        text = TextMobject("This is the arbitrage!")
        self.play(Transform(formula, text))


