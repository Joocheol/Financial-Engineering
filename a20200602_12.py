from manimlib.imports import *

class a20200602_12(Scene):
    def construct(self):
        #self.draw_border()
        #self.start()
        self.hard_way()
        #self.in_general()

    

    def in_general(self):
        s = r"""In general"""
        t_1 = TextMobject(s)

        self.play(Write(t_1))
        self.wait()
        self.play(t_1.to_corner, UL, buff=1)

        s = r"""e^x= 1 +\frac{x}{1!} +\frac{x^2}{2!} +\frac{x^3}{3!} +\frac{x^4}{4!} +\cdots""".split()
        f_1 = TexMobject(*s)

        self.play(Write(f_1))
        self.wait(2)
        self.play(f_1.shift,UP*1.5)

        s = r"""e^x= 1 +x +\frac{x^2}{2\cdot{1}} +\frac{x^3}{3\cdot{2}\cdot{1}} 
            +\frac{x^4}{4\cdot{3}\cdot{2}\cdot{1}} +\cdots""".split()
        f_2 = TexMobject(*s)

        self.play(Write(f_2[0:1]))
        self.play(LaggedStart(
            TransformFromCopy(f_1[1], f_2[1]),
            TransformFromCopy(f_1[2], f_2[2]),
            TransformFromCopy(f_1[3], f_2[3]),
            TransformFromCopy(f_1[4], f_2[4]),
            TransformFromCopy(f_1[5], f_2[5]),
            TransformFromCopy(f_1[6], f_2[6]),
            lag_ratio=0.9
            ))
        self.wait(2)
        self.play(FadeOut(f_1))
        self.play(f_2.shift,UP*1.5)

        s = r"""e^x= 1 +x +\frac{x^2}{2} +\frac{x^3}{6} 
            +\frac{x^4}{24} +\cdots""".split()
        f_3 = TexMobject(*s)

        self.play(Write(f_3[0:1]))
        self.play(LaggedStart(
            TransformFromCopy(f_2[1], f_3[1]),
            TransformFromCopy(f_2[2], f_3[2]),
            TransformFromCopy(f_2[3], f_3[3]),
            TransformFromCopy(f_2[4], f_3[4]),
            TransformFromCopy(f_2[5], f_3[5]),
            TransformFromCopy(f_2[6], f_3[6]),
            lag_ratio=0.9
            ))
        self.wait(2)
        self.play(FadeOut(f_2))
        self.play(f_3.shift,UP*1.5)
    
    def hard_way(self):
        s = r"""A hard way first"""
        t_1 = TextMobject(s)
        self.play(Write(t_1))
        self.wait()
        self.play(t_1.to_corner, UL, buff=1)

        s = r"""e= 1 +\frac{1}{1!} +\frac{1}{2!} +\frac{1}{3!} 
        +\frac{1}{4!} +\cdots""".split() 
        f_1 = TexMobject(*s)
        self.play(Write(f_1))
        # self.wait(2)
        # self.play(f_1.shift,UP*1.5)

        # s = r"""e= 1 +\frac{1}{1} +\frac{1}{2\cdot{1}} +\frac{1}{3\cdot{2}\cdot{1}} 
        #     +\frac{1}{4\cdot{3}\cdot{2}\cdot{1}} +\cdots""".split()
        # f_2 = TexMobject(*s)
        # self.play(Write(f_2[0:1]))
        # self.play(LaggedStart(
        #     TransformFromCopy(f_1[1], f_2[1]),
        #     TransformFromCopy(f_1[2], f_2[2]),
        #     TransformFromCopy(f_1[3], f_2[3]),
        #     TransformFromCopy(f_1[4], f_2[4]),
        #     TransformFromCopy(f_1[5], f_2[5]),
        #     TransformFromCopy(f_1[6], f_2[6]),
        #     lag_ratio=0.9
        #     ))
        # self.wait(2)
        # self.play(FadeOut(f_1))
        # self.play(f_2.shift,UP*1.5)

        # brace_1 = Brace(f_2[1], DOWN, buff=SMALL_BUFF)
        # s = r"""e= 1""".split()
        # f_3 = TexMobject(*s)
        # self.play(Write(f_3[0]))
        # self.play(ShowCreation(brace_1))
        # self.play(ReplacementTransform(f_2[1:2].copy(), f_3[0:2]))

        # brace_2 = Brace(f_2[1:3], DOWN, buff=SMALL_BUFF)
        # s = r"""e= 2""".split()
        # f_4 = TexMobject(*s)
        # self.play(Transform(brace_1, brace_2))
        # self.play(LaggedStart(
        #     ReplacementTransform(f_2[1:3].copy(), f_4[1:2]), 
        #     ReplacementTransform(f_3[0:2], f_4[0:2]),
        #     lag_ratio=0.9
        #     ))

        # brace_2 = Brace(f_2[1:4], DOWN, buff=SMALL_BUFF)
        # s = r"""e= 2.5""".split()
        # f_5 = TexMobject(*s)
        # self.play(Transform(brace_1, brace_2))
        # self.play(LaggedStart(
        #     ReplacementTransform(f_2[1:4].copy(), f_5[1:2]), 
        #     Transform(f_4[0:2], f_5[0:2]),
        #     lag_ratio=0.9
        #     ))
        
        #self.play(FadeOut(t_1), FadeOut(f_2))

        

    def start(self):
        s = r"""What is $e$?"""
        t_1 = TextMobject(s)

        self.play(Write(t_1))
        self.wait()
        self.play(FadeOut(t_1))

    def draw_border(self):
        border = Rectangle(width=FRAME_WIDTH, height=FRAME_HEIGHT, stroke_color=YELLOW)
        self.add(border)


