from manimlib.imports import *

class a20200419(Scene):
    def construct(self):

        S = TexMobject("S")
        S_u = TexMobject("u S")
        S_d = TexMobject("d S")

        S.move_to(LEFT+DOWN)
        S_u.move_to(RIGHT)
        S_d.move_to(RIGHT+DOWN*2)

        arrow_u = Arrow(S.get_right(), S_u.get_left(), buff=0.5)
        arrow_d = Arrow(S.get_right(), S_d.get_left(), buff=0.5)

        self.play(Write(S))
        self.play(GrowArrow(arrow_u))
        self.play(Write(S_u))
        self.play(GrowArrow(arrow_d))
        self.play(Write(S_d))
        self.play(FadeOut(arrow_u), FadeOut(arrow_d))

        SS = TexMobject("S")
        SS_u = TexMobject("u S")
        SS_d = TexMobject("d S")
        SS.scale(0.7).move_to(LEFT*6+UP*2.5)
        SS_u.scale(0.7).move_to(LEFT*5+UP*3.5)
        SS_d.scale(0.7).move_to(LEFT*5+UP*1.5)

        self.play(Transform(S, SS), Transform(S_u, SS_u), Transform(S_d, SS_d))
        
        r = TexMobject("1")
        r_u = TexMobject("r")
        r_d = TexMobject("r")

        r.move_to(LEFT+DOWN)
        r_u.move_to(RIGHT)
        r_d.move_to(RIGHT+DOWN*2)

        arrow_u = Arrow(r.get_right(), r_u.get_left(), buff=0.5)
        arrow_d = Arrow(r.get_right(), r_d.get_left(), buff=0.5)

        self.play(Write(r))
        self.play(GrowArrow(arrow_u))
        self.play(Write(r_u))
        self.play(GrowArrow(arrow_d))
        self.play(Write(r_d))
        self.play(FadeOut(arrow_u), FadeOut(arrow_d))

        rr = TexMobject("1")
        rr_u = TexMobject("r")
        rr_d = TexMobject("r")
        rr.scale(0.7).move_to(LEFT*1+UP*2.5)
        rr_u.scale(0.7).move_to(RIGHT*0+UP*3.5)
        rr_d.scale(0.7).move_to(RIGHT*0+UP*1.5)

        self.play(Transform(r, rr), Transform(r_u, rr_u), Transform(r_d, rr_d))

        C = TexMobject("C")
        C_u = TexMobject("C_u = \\max (uS - K, 0)")
        C_d = TexMobject("C_d = \\max (dS - K, 0)")

        C.move_to(LEFT*2+DOWN)
        C_u.move_to(RIGHT*2)
        C_d.move_to(RIGHT*2+DOWN*2)

        arrow_u = Arrow(C.get_right(), C_u.get_left(), buff=0.5)
        arrow_d = Arrow(C.get_right(), C_d.get_left(), buff=0.5)

        self.play(Write(C))
        self.play(GrowArrow(arrow_u))
        self.play(Write(C_u))
        self.play(GrowArrow(arrow_d))
        self.play(Write(C_d))
        self.play(FadeOut(arrow_u), FadeOut(arrow_d))

        CC = TexMobject("?")
        CC_u = TexMobject("C_u")
        CC_d = TexMobject("C_d")
        CC.scale(0.7).move_to(RIGHT*4+UP*2.5)
        CC_u.scale(0.7).move_to(RIGHT*5+UP*3.5)
        CC_d.scale(0.7).move_to(RIGHT*5+UP*1.5)

        self.play(Transform(C, CC), Transform(C_u, CC_u), Transform(C_d, CC_d))

        condition = TexMobject("d < r < u")
        self.play(Write(condition))
        self.wait(2)
        