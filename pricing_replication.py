from manimlib.imports import *

class text(Scene):
    def construct(self):

############
        game1 = Tex("10")
        game1_up = Tex("11")
        game1_down = Tex("11")

        game2 = Tex("9")
        game2_up = Tex("22")
        game2_down = Tex("0")

        game3 = Tex("?")
        game3_up = Tex("22")
        game3_down = Tex("11")

        self.play(Write(game1.scale(0.7).move_to([-6,2,0])))
        self.play(Write(game1_up.scale(0.7).move_to([-4,3,0])))
        self.play(Write(game1_down.scale(0.7).move_to([-4,1,0])))
        self.wait(1)

        self.play(Write(game2.scale(0.7).move_to([-1,2,0])))
        self.play(Write(game2_up.scale(0.7).move_to([1,3,0])))
        self.play(Write(game2_down.scale(0.7).move_to([1,1,0])))
        self.wait(1)

        self.play(Write(game3.scale(0.7).move_to([4,2,0])))
        self.play(Write(game3_up.scale(0.7).move_to([6,3,0])))
        self.play(Write(game3_down.scale(0.7).move_to([6,1,0])))
        self.wait(1)

##########
        rect = Rectangle(height=2.5, width=1.0)
        self.play(ShowCreation(rect.move_to([-4, 2, 0])))
        self.wait(1)

##########
        formula = Tex(r"""
        \begin{bmatrix} 11 \\ 11 \end{bmatrix}
        \times x_1
        \begin{bmatrix} 11 \\ 11 \end{bmatrix}
        =
        \begin{bmatrix} 11 \\ 11 \end{bmatrix}        
        """)
        
        self.add(formula)
        self.wait(1)

