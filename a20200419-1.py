from manimlib.imports import *

class a20200419_1(Scene):
    def construct(self):

        SS = TexMobject("S")
        SS_u = TexMobject("u S")
        SS_d = TexMobject("d S")
        SS.scale(0.7).move_to(LEFT*6+UP*2.5)
        SS_u.scale(0.7).move_to(LEFT*5+UP*3.5)
        SS_d.scale(0.7).move_to(LEFT*5+UP*1.5)

        
        rr = TexMobject("1")
        rr_u = TexMobject("r")
        rr_d = TexMobject("r")
        rr.scale(0.7).move_to(LEFT*1+UP*2.5)
        rr_u.scale(0.7).move_to(RIGHT*0+UP*3.5)
        rr_d.scale(0.7).move_to(RIGHT*0+UP*1.5)

        CC = TexMobject("?")
        CC_u = TexMobject("C_u")
        CC_d = TexMobject("C_d")
        CC.scale(0.7).move_to(RIGHT*4+UP*2.5)
        CC_u.scale(0.7).move_to(RIGHT*5+UP*3.5)
        CC_d.scale(0.7).move_to(RIGHT*5+UP*1.5)

        self.play(
            Write(SS), Write(SS_u), Write(SS_d), 
            Write(rr), Write(rr_u), Write(rr_d),
            Write(CC), Write(CC_u), Write(CC_d))

        rect1 = Rectangle(height=2.5, width=1)
        rect1.set_color(YELLOW)
        rect1.move_to(LEFT*5+UP*2.5)
        self.play(ShowCreation(rect1))

        rect2 = Rectangle(height=2.5, width=1)
        rect2.set_color(RED)
        rect2.move_to(LEFT*0+UP*2.5)
        self.play(ShowCreation(rect2))

        rect3 = Rectangle(height=2.5, width=1)
        rect3.set_color(BLUE)
        rect3.move_to(RIGHT*5+UP*2.5)
        self.play(ShowCreation(rect3))

        formula_1 = TexMobject(r"""
            \begin{bmatrix} uS \\ \\ dS \end{bmatrix}
            \times
            \Delta
            +
            \begin{bmatrix} r \\ \\ r \end{bmatrix}
            \times
            B
            =
            \begin{bmatrix} C_u \\ \\ C_d \end{bmatrix} 
        """)
        
        formula_1.move_to(DOWN)
        self.play(Write(formula_1))
        self.wait(2)

        formula_2 = TexMobject(r"""
            \Delta 
            =
            {C_u - C_d 
            \over
            (u-d) S}
            ,
            \quad
            B
            =
            {u C_d - d C_u
            \over
            (u-d) r}
        """
        )
        formula_2.move_to(DOWN)
        self.play(Transform(formula_1, formula_2))
        self.wait(2)

        self.play(FadeOut(rect1), FadeOut(rect2), FadeOut(rect3))

        rect1 = Rectangle(height=1, width=1)
        rect1.set_color(YELLOW)
        rect1.move_to(LEFT*6+UP*2.5)
        self.play(ShowCreation(rect1))

        rect2 = Rectangle(height=1, width=1)
        rect2.set_color(RED)
        rect2.move_to(LEFT*1+UP*2.5)
        self.play(ShowCreation(rect2))

        rect3 = Rectangle(height=1, width=1)
        rect3.set_color(BLUE)
        rect3.move_to(RIGHT*4+UP*2.5)
        self.play(ShowCreation(rect3))

        self.play(FadeOut(formula_1), Write(formula_2.move_to(UP).scale(0.5)))

        formula_3 = TexMobject(r"""
            C = S \times 
            \Delta
            +
            1
            \times
            B
        """)
        self.play(Write(formula_3.shift(DOWN*1.5)))
#        self.play(Transform(formula_1, formula_2.move_to(UP*2).scale(0.5)))
        self.play(Transform(formula_1, formula_3.move_to(UP*0.5).scale(0.5)))

        formula_4 = TexMobject(r"""
            C = S \times 
            {C_u - C_d 
            \over
            (u-d) S}
            +
            1
            \times
            {u C_d - d C_u
            \over
            (u-d) r}
        """)
        self.play(Write(formula_4.shift(DOWN*1.5)))
        self.wait(1)

        # S = TexMobject("S")
        # S_u = TexMobject("u S")
        # S_d = TexMobject("d S")

        # S.move_to(LEFT+DOWN)
        # S_u.move_to(RIGHT)
        # S_d.move_to(RIGHT+DOWN*2)

        # arrow_u = Arrow(S.get_right(), S_u.get_left(), buff=0.5)
        # arrow_d = Arrow(S.get_right(), S_d.get_left(), buff=0.5)

        # self.play(Write(S))
        # self.play(GrowArrow(arrow_u))
        # self.play(Write(S_u))
        # self.play(GrowArrow(arrow_d))
        # self.play(Write(S_d))
        # self.play(FadeOut(arrow_u), FadeOut(arrow_d))

        
        
        # r = TexMobject("1")
        # r_u = TexMobject("r")
        # r_d = TexMobject("r")

        # r.move_to(LEFT+DOWN)
        # r_u.move_to(RIGHT)
        # r_d.move_to(RIGHT+DOWN*2)

        # arrow_u = Arrow(r.get_right(), r_u.get_left(), buff=0.5)
        # arrow_d = Arrow(r.get_right(), r_d.get_left(), buff=0.5)

        # self.play(Write(r))
        # self.play(GrowArrow(arrow_u))
        # self.play(Write(r_u))
        # self.play(GrowArrow(arrow_d))
        # self.play(Write(r_d))
        # self.play(FadeOut(arrow_u), FadeOut(arrow_d))

        

        # C = TexMobject("C")
        # C_u = TexMobject("C_u = \\max (uS - K, 0)")
        # C_d = TexMobject("C_d = \\max (dS - K, 0)")

        # C.move_to(LEFT*2+DOWN)
        # C_u.move_to(RIGHT*2)
        # C_d.move_to(RIGHT*2+DOWN*2)

        # arrow_u = Arrow(C.get_right(), C_u.get_left(), buff=0.5)
        # arrow_d = Arrow(C.get_right(), C_d.get_left(), buff=0.5)

        # self.play(Write(C))
        # self.play(GrowArrow(arrow_u))
        # self.play(Write(C_u))
        # self.play(GrowArrow(arrow_d))
        # self.play(Write(C_d))
        # self.play(FadeOut(arrow_u), FadeOut(arrow_d))

        