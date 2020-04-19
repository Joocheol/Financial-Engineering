from manimlib.imports import *

class a20200419_2(Scene):
    def construct(self):

    	S = TexMobject("S")
    	S_u = TexMobject("u S")
    	S_d = TexMobject("d S")
    	S_uu = TexMobject("u^2 S")
    	S_ud = TexMobject("u d S")
    	S_dd = TexMobject("d^2 S")

    	S.move_to(LEFT*5)
    	S_u.move_to(LEFT*3+UP*1)
    	S_d.move_to(LEFT*3+DOWN*1)
    	S_uu.move_to(LEFT*1+UP*2)
    	S_ud.move_to(LEFT*1+UP*0)
    	S_dd.move_to(LEFT*1+DOWN*2)


    	arrow_u = Arrow(S.get_right(), S_u.get_left(), buff=0.5)
    	arrow_d = Arrow(S.get_right(), S_d.get_left(), buff=0.5)
    	arrow_uu = Arrow(S_u.get_right(), S_uu.get_left(), buff=0.5)
    	arrow_ud = Arrow(S_u.get_right(), S_ud.get_left(), buff=0.5)
    	arrow_du = Arrow(S_d.get_right(), S_ud.get_left(), buff=0.5)
    	arrow_dd = Arrow(S_d.get_right(), S_dd.get_left(), buff=0.5)


    	self.play(Write(S))
    	self.play(GrowArrow(arrow_u))
    	self.play(Write(S_u))
    	self.play(GrowArrow(arrow_d))
    	self.play(Write(S_d))
    	self.play(GrowArrow(arrow_uu))
    	self.play(Write(S_uu))
    	self.play(GrowArrow(arrow_ud))
    	self.play(Write(S_ud))
    	self.play(GrowArrow(arrow_du))
    	self.play(GrowArrow(arrow_dd))
    	self.play(Write(S_dd))

    	r = TexMobject("1")
    	r_u = TexMobject("r")
    	r_d = TexMobject("r")
    	r_uu = TexMobject("r^2")
    	r_ud = TexMobject("r^2")
    	r_dd = TexMobject("r^2")

    	r.move_to(RIGHT*1)
    	r_u.move_to(RIGHT*3+UP*1)
    	r_d.move_to(RIGHT*3+DOWN*1)
    	r_uu.move_to(RIGHT*5+UP*2)
    	r_ud.move_to(RIGHT*5+UP*0)
    	r_dd.move_to(RIGHT*5+DOWN*2)


    	arrow_u = Arrow(r.get_right(), r_u.get_left(), buff=0.5)
    	arrow_d = Arrow(r.get_right(), r_d.get_left(), buff=0.5)
    	arrow_uu = Arrow(r_u.get_right(), r_uu.get_left(), buff=0.5)
    	arrow_ud = Arrow(r_u.get_right(), r_ud.get_left(), buff=0.5)
    	arrow_du = Arrow(r_d.get_right(), r_ud.get_left(), buff=0.5)
    	arrow_dd = Arrow(r_d.get_right(), r_dd.get_left(), buff=0.5)


    	self.play(Write(r))
    	self.play(GrowArrow(arrow_u))
    	self.play(Write(r_u))
    	self.play(GrowArrow(arrow_d))
    	self.play(Write(r_d))
    	self.play(GrowArrow(arrow_uu))
    	self.play(Write(r_uu))
    	self.play(GrowArrow(arrow_ud))
    	self.play(Write(r_ud))
    	self.play(GrowArrow(arrow_du))
    	self.play(GrowArrow(arrow_dd))
    	self.play(Write(r_dd))
    	self.play(FadeOut(r), FadeOut(r_u), FadeOut(r_d), 
    		FadeOut(r_uu), FadeOut(r_ud), FadeOut(r_dd),
    		FadeOut(arrow_u), FadeOut(arrow_d), FadeOut(arrow_uu),
    		FadeOut(arrow_ud), FadeOut(arrow_du),FadeOut(arrow_dd)
    	)
    	C = TexMobject("?")
    	C_u = TexMobject("?")
    	C_d = TexMobject("?")
    	C_uu = TexMobject("C_{uu}")
    	C_ud = TexMobject("C_{ud}")
    	C_dd = TexMobject("C_{dd}")

    	C.move_to(RIGHT*1)
    	C_u.move_to(RIGHT*3+UP*1)
    	C_d.move_to(RIGHT*3+DOWN*1)
    	C_uu.move_to(RIGHT*5+UP*2)
    	C_ud.move_to(RIGHT*5+UP*0)
    	C_dd.move_to(RIGHT*5+DOWN*2)


    	arrow_u = Arrow(C.get_right(), C_u.get_left(), buff=0.5)
    	arrow_d = Arrow(C.get_right(), C_d.get_left(), buff=0.5)
    	arrow_uu = Arrow(C_u.get_right(), C_uu.get_left(), buff=0.5)
    	arrow_ud = Arrow(C_u.get_right(), C_ud.get_left(), buff=0.5)
    	arrow_du = Arrow(C_d.get_right(), C_ud.get_left(), buff=0.5)
    	arrow_dd = Arrow(C_d.get_right(), C_dd.get_left(), buff=0.5)


    	self.play(Write(C))
    	self.play(GrowArrow(arrow_u))
    	self.play(Write(C_u))
    	self.play(GrowArrow(arrow_d))
    	self.play(Write (C_d))
    	self.play(GrowArrow(arrow_uu))
    	self.play(Write(C_uu))
    	self.play(GrowArrow(arrow_ud))
    	self.play(Write(C_ud))
    	self.play(GrowArrow(arrow_du))
    	self.play(GrowArrow(arrow_dd))
    	self.play(Write(C_dd))
