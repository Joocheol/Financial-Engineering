from manimlib.imports import *

class a20200531_15(Scene):
    def construct(self):

#1
        t_1 = TextMobject("What is $e$?")
        self.play(Write(t_1))
        self.wait(2)
        self.play(FadeOut(t_1))

#2
        t_1 = TextMobject("A hard way first")
        string = r"e= 1 +\frac{1}{1!} +\frac{1}{2!} +\frac{1}{3!} +\frac{1}{4!} +\cdots".split()
        f_1 = TexMobject(*string)
        string = r"e= 1 +\frac{1}{1} +\frac{1}{2\cdot{1}} +\frac{1}{3\cdot{2}\cdot{1}} +\frac{1}{4\cdot{3}\cdot{2}\cdot{1}} +\cdots".split()
        f_1_1 = TexMobject(*string)
        string = r"e= 1 +\frac{1}{1} +\frac{1}{2} +\frac{1}{6} +\frac{1}{24} +\cdots".split()
        f_2 = TexMobject(*string)
        string = r"e= 2 +\frac{1}{2} +\frac{1}{6} +\frac{1}{24} +\frac{1}{120} +\cdots".split()
        f_3 = TexMobject(*string)
        string = r"e= 2.5 +\frac{1}{6} +\frac{1}{24} +\frac{1}{120} +\frac{1}{720} +\cdots".split()
        f_4 = TexMobject(*string)
        string = r"e= 2.67 +\frac{1}{24} +\frac{1}{120} +\frac{1}{720} +\frac{1}{5040} +\cdots".split()
        f_5 = TexMobject(*string)
        string = r"e= 2.71 +\frac{1}{120} +\frac{1}{720} +\frac{1}{5040} +\frac{1}{40320} +\cdots".split()
        f_6 = TexMobject(*string)
        
        
        self.play(Write(t_1))
        self.wait()
        self.play(t_1.to_edge,UL,buff=1)
        
        self.play(Write(f_1))
        self.wait(1)
        self.play(f_1.shift, UP*1.5)
        self.play(Write(f_1_1[0]))
        self.play(LaggedStart(
            TransformFromCopy(f_1[1], f_1_1[1]),
            TransformFromCopy(f_1[2], f_1_1[2]),
            TransformFromCopy(f_1[3], f_1_1[3]),
            TransformFromCopy(f_1[4], f_1_1[4]),
            TransformFromCopy(f_1[5], f_1_1[5]),
            TransformFromCopy(f_1[6], f_1_1[6]),
            lag_ratio=0.9,
        ))
        self.wait(2)
        self.play(ReplacementTransform(f_1_1, f_2))
        self.wait(2)
        self.play(FadeOut(f_1), f_2.shift, UP*1.5)
        self.wait(2)

        self.play(Write(f_3[0]))
        self.play(LaggedStart(
            TransformFromCopy(f_2[1:3], f_3[1:2]),
            TransformFromCopy(f_2[3], f_3[2]),
            TransformFromCopy(f_2[4], f_3[3]),
            TransformFromCopy(f_2[5], f_3[4]),
            TransformFromCopy(f_2[6], f_3[5:7]),
            lag_ratio=0.9,
        ))
        self.wait(2)
        self.play(ReplacementTransform(f_1_1, f_2))
        self.wait(2)
        self.play(ReplacementTransform(f_2, f_3))
        self.wait(2)
        self.play(ReplacementTransform(f_3, f_4))
        self.wait(2)
        self.play(ReplacementTransform(f_4, f_5))
        self.wait(2)

        self.play(FadeOut(t_1), FadeOut(f_5))

#3
        t_1 = TextMobject("In general,")
        f_1 = TexMobject(r"e^x = 1 + \frac{x}{1!} + \frac{x}{2!} + \frac{x}{3!} + \frac{x}{4!} + \cdots")
        f_2 = TexMobject(r"e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots")
        
        self.play(Write(t_1))
        self.play(t_1.to_edge,UL,buff=1)
        
        self.play(Write(f_1))
        self.wait(2)
        self.play(ReplacementTransform(f_1, f_2))
        self.wait(2)

        self.play(FadeOut(t_1), FadeOut(f_2))

#4
        t_1 = TextMobject("The derivative of $e^x$ is $e^x$ itself. Here is why.")
        f_1 = TexMobject(r"e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots")
        f_2 = TexMobject(r"\frac{d}{dx} e^x = \frac{d}{dx} 1 + \frac{d}{dx} x + \frac{d}{dx} \frac{x^2}{2} + \frac{d}{dx} \frac{x^3}{6} + \frac{d}{dx} \frac{x^4}{24} + \cdots")
        f_3 = TexMobject(r"\frac{d}{dx} e^x = 0 + 1 + x + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots")
        g = VGroup(f_1,f_2,f_3).arrange(DOWN, buff=0.5)

        self.play(Write(t_1))
        self.play(t_1.to_edge,UL,buff=1)
        
        self.play(Write(g[0]))
        self.wait(2)
        self.play(Write(g[1]))
        self.wait(2)
        self.play(Write(g[2]))

        self.wait(2)

        self.play(FadeOut(g), FadeOut(t_1))
        

#3
        # t_1 = TextMobject("1. 100\% interest paid every year.")
        # t_2 = TextMobject("2. 50\% interest paid every 6 months.")
        # g = VGroup(t_1,t_2).arrange(DOWN, aligned_edge = LEFT,  buff = 0.5)
        # self.play(Write(g))
        # self.wait(2)
        # self.play(FadeOut(g))



 