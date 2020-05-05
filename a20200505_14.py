from manimlib.imports import *

class a20200505_14(Scene):
    def construct(self):

        f_1 = TexMobject("(x+y)^2", "=", "x^2", "+", "2xy", "+", "y^2")
        f_1.move_to(UP*2)
        self.play(Write(f_1))
        self.wait()

        f_2 = TexMobject("(x+y)^3", "=", "x^3 + 3 x^2 y + 3 x y^2 + y^3 ")
        f_2.move_to(UP*1)
        self.play(Write(f_2))
        self.wait()

        f_3 = TexMobject("(x+y)^3", "=", "{3 \\choose 0} x^3 y^0 + {3 \\choose 1} x^2 y^1 +", 
        	"{3 \\choose 2} x^1 y^2 + {3 \\choose 3} x^0 y^3 ")
        f_3.move_to(DOWN*0.5)
        self.play(Write(f_3))
        self.wait()

        F_4 = TexMobject("{n \\choose k} = { {n!} \\over {k! (n-k)!} },", 
        	"\\quad n! = n \\times (n-1) \\times\\cdots \\times 1 ")
        F_4.move_to(DOWN*2)
        self.play(Write(F_4))
        self.wait()



