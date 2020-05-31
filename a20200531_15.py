from manimlib.imports import *

class a20200531_15(Scene):
    def construct(self):

#1
        t_1 = TextMobject("What is $e$?")
        self.play(Write(t_1))
        self.wait(2)
        self.play(FadeOut(t_1))

#2
        t_1 = TextMobject("A hard way first").to_edge(UL, buff=1)
        f_1 = TexMobject(r"e = 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \cdots")
        f_2 = TexMobject(r"e = 1 + \frac{1}{1} + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \cdots")
        
        self.add(t_1)
        
        self.play(Write(f_1))
        self.play(ReplacementTransform(f_1, f_2))
        self.wait(2)

        self.play(FadeOut(t_1), FadeOut(f_2))

#3
        t_1 = TextMobject("In general").to_edge(UL, buff=1)
        f_1 = TexMobject(r"e^x = 1 + \frac{x}{1!} + \frac{x}{2!} + \frac{x}{3!} + \frac{x}{4!} + \cdots")
        f_2 = TexMobject(r"e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots")
        
        self.add(t_1)
        
        self.play(Write(f_1))
        self.play(ReplacementTransform(f_1, f_2))
        self.wait(2)

        self.play(FadeOut(t_1), FadeOut(f_2))

#3
        t_1 = TextMobject("1. 100\% interest paid every year.")
        t_2 = TextMobject("2. 50\% interest paid every 6 months.")
        g = VGroup(t_1,t_2).arrange(DOWN, aligned_edge = LEFT,  buff = 0.5)
        self.play(Write(g))
        self.wait(2)
        self.play(FadeOut(g))



 