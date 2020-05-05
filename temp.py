from manimlib.imports import *
import math

class Pascal_s_triangle(Scene):
    def construct(self):

        for i in range(1,8):
            for j in range(i+1):
                binom = int(math.factorial(i)/(math.factorial(j) * math.factorial(i-j)))
                f = TexMobject("{}".format(binom))
                f.move_to([0,4,0] + DOWN*i + RIGHT*(j-i/2))
                self.play(Write(f), run_time = 0.3)
        
        self.wait()



