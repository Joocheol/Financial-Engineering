from manimlib.imports import *

class a20200603_11(Scene):
    def construct(self):
        #self.start()
        #self.hard_way()
        #self.in_general()
        self.derivative()

    def derivative(self):
        t_1 = TextMobject(r"""We know that \\
            the derivative of $e^x$ with repect to $x$ \\ is the original function, $e^x$, itself. \\ But why?""")
        self.play(Write(t_1))
        self.wait(2)
        self.play(FadeOut(t_1))

        s = r"""\frac{d}{dx} e^x= \frac{d}{dx} \Big( 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \Big)""".split()
        f_1 = Tex(*s)
        self.play(Write(f_1))
        self.wait()
        self.play(f_1.move_to, UP*0.5)

        


        
    def in_general(self):
        t_1 = TextMobject("In general")
        self.play(Write(t_1))
        self.wait()
        self.play(t_1.to_edge, UL-DOWN, buff=1)

        s = r"""e^x= 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots""".split()
        f_1 = Tex(*s)
        self.play(Write(f_1))
        self.wait()
        
        self.play(FadeOut(t_1), FadeOut(f_1))

    def hard_way(self):
        
        t_1 = TextMobject("A hard way first")
        self.play(Write(t_1))
        self.wait()
        self.play(t_1.to_edge, UL-DOWN, buff=1)
        
        s = r"e= 1 +\frac{1}{1!} +\frac{1}{2!} +\frac{1}{3!} +\frac{1}{4!} +\frac{1}{5!} +\cdots".split()
        f_1 = Tex(*s)
        self.play(Write(f_1))
        self.wait()
        self.play(f_1.move_to, [0,0.5,0])

        s = r"""e= 1 +\frac{1}{1} +\frac{1}{2\cdot{1}} +\frac{1}{3\cdot{2}\cdot{1}} 
            +\frac{1}{4\cdot{3}\cdot{2}\cdot{1}} +\frac{1}{5\cdot{4}\cdot{3}\cdot{2}\cdot{1}} +\cdots""".split()
        f_2 = Tex(*s)
        f_2.next_to(f_1, DOWN, buff=0.5)
        self.play(Write(f_2[0]))
        self.play(LaggedStart(
            TransformFromCopy(f_1[1], f_2[1]),
            TransformFromCopy(f_1[2], f_2[2]),
            TransformFromCopy(f_1[3], f_2[3]),
            TransformFromCopy(f_1[4], f_2[4]),
            TransformFromCopy(f_1[5], f_2[5]),
            TransformFromCopy(f_1[6], f_2[6]),
            TransformFromCopy(f_1[7], f_2[7]),
            lag_ratio=0.9,
        ))
        self.remove(f_1)
        self.play(f_2.move_to, [0,0.5,0])

        s = r"""e= 1 +1 +\frac{1}{2} +\frac{1}{6} +\frac{1}{24} +\frac{1}{120} +\cdots""".split()
        f_3 = Tex(*s)
        f_3.next_to(f_2, DOWN, buff=0.5)
        self.play(Write(f_3[0]))
        self.play(LaggedStart(
            TransformFromCopy(f_2[1], f_3[1]),
            TransformFromCopy(f_2[2], f_3[2]),
            TransformFromCopy(f_2[3], f_3[3]),
            TransformFromCopy(f_2[4], f_3[4]),
            TransformFromCopy(f_2[5], f_3[5]),
            TransformFromCopy(f_2[6], f_3[6]),
            TransformFromCopy(f_2[7], f_3[7]),
            lag_ratio=0.9,
        ))
        self.remove(f_2)
        self.play(f_3.move_to, [0,0.5,0])

        brace_1 = Brace(f_3[1:3],DOWN,buff=SMALL_BUFF)
        s = s = r"""e\approx 2""".split()
        f_4 = Tex(*s)
        f_4.next_to(f_3, DOWN, buff=0.5)
        self.play(ShowCreation(brace_1))
        self.play(Write(f_4))

        brace_2 = Brace(f_3[1:4],DOWN,buff=SMALL_BUFF)
        s = s = r"""e\approx 2.5""".split()
        f_5 = Tex(*s)
        f_5.next_to(f_3, DOWN, buff=0.5)
        self.play(Transform(brace_1, brace_2))
        self.play(Transform(f_4, f_5))

        brace_2 = Brace(f_3[1:5],DOWN,buff=SMALL_BUFF)
        s = s = r"""e\approx 2.667""".split()
        f_5 = Tex(*s)
        f_5.next_to(f_3, DOWN, buff=0.5)
        self.play(Transform(brace_1, brace_2))
        self.play(Transform(f_4, f_5))

        brace_2 = Brace(f_3[1:6],DOWN,buff=SMALL_BUFF)
        s = s = r"""e\approx 2.7083""".split()
        f_5 = Tex(*s)
        f_5.next_to(f_3, DOWN, buff=0.5)
        self.play(Transform(brace_1, brace_2))
        self.play(Transform(f_4, f_5))

        brace_2 = Brace(f_3[1:7],DOWN,buff=SMALL_BUFF)
        s = s = r"""e\approx 2.71667""".split()
        f_5 = Tex(*s)
        f_5.next_to(f_3, DOWN, buff=0.5)
        self.play(Transform(brace_1, brace_2))
        self.play(Transform(f_4, f_5))

        brace_2 = Brace(f_3[1:8],DOWN,buff=SMALL_BUFF)
        s = s = r"""e= 2.71828\cdots""".split()
        f_5 = Tex(*s)
        f_5.next_to(f_3, DOWN, buff=0.5)
        self.play(Transform(brace_1, brace_2))
        self.play(Transform(f_4, f_5))
        self.wait()

        self.play(FadeOut(t_1), FadeOut(f_4), FadeOut(brace_1), FadeOut(f_3))

    def start(self):
        t_1 = TextMobject("What is $e$?")
        self.play(Write(t_1))
        self.wait(2)
        self.play(FadeOut(t_1))