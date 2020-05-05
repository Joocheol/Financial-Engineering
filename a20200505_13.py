from manimlib.imports import *
import math

class Pascal_s_triangle(Scene):
    def construct(self):

        b_all = []

        for i in range(1,8):
            for j in range(i+1):
                binom = int(math.factorial(i)/(math.factorial(j) * math.factorial(i-j)))
                f = TexMobject("{}".format(binom))
                f.move_to([0,4,0] + DOWN*i + RIGHT*(j-i/2))
                self.play(Write(f), run_time = 0.2)
                b_all.append(f)
        
        b_g = VGroup(*b_all)
        self.wait()

        c_all = []

        for i in range(1,8):
            for j in range(i+1):
                f = TexMobject("{} \\choose {}".format(i, j))
                f.move_to([0,4,0] + DOWN*i + RIGHT*(j-i/2)).scale(0.7)
                #self.play(Write(f), run_time = 0.3)
                c_all.append(f)
        c_g = VGroup(*c_all)

        self.play(Transform(b_g, c_g))
        self.wait()



