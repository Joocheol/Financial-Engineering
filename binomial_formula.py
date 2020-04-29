from manimlib.imports import *

class binomial_formula(Scene):
    def construct(self):

        f_1 = TexMobject("(a+b)^2", "=", "a^2", "+", "2ab", "+", "b^2")
        f_1.move_to(UP*2)
        self.play(Write(f_1))
        self.wait(3)

        f_2 = TexMobject("(a+b)^3", "=", "a^3 + 3 a^2 b + 3 a b^2 + b^3 ")
        f_2.move_to(UP*1)
        self.play(Write(f_2))
        self.wait(3)

        f_3 = TexMobject("(a+b)^3", "=", "{3 \\choose 0} a^3 b^0 + {3 \\choose 1} 3 a^2 b^1 +", 
        	"{3 \\choose 2} 3 a^1 b^2 + {3 \\choose 3} a^0 b^3 ")
        f_3.move_to(DOWN*0.5)
        self.play(Write(f_3))
        self.wait(3)

        F_4 = TexMobject("{n \\choose x} = { {n!} \\over {x! (n-x)!} },", 
        	"\\quad n! = n \\times (n-1) \\times\\cdots \\times 1 ")
        F_4.move_to(DOWN*2)
        self.play(Write(F_4))
        self.wait(3)



