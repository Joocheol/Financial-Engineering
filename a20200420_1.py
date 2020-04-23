from manimlib.imports import *

class a20200420_1(Scene):
    def construct(self):

        text = TextMobject("1 Step:")
        text.move_to(UP*3+LEFT*4)
        self.play(Write(text))

        formula_1 = TexMobject(
            "C", "=", "{1 \\over r }", 
            "\\Big[", "p", "C_{u}", "+", "(1-p)", "C_{d}", "\\Big]"  
        )

        formula_1.move_to(UP*2.5).scale(0.7)
        
        self.play(Write(formula_1))
        self.wait()

        text = TextMobject("2 Steps:")
        text.move_to(UP*2+LEFT*4)
        self.play(Write(text))
        
        formula_2 = TexMobject(
            "C", "=", "{1 \\over r^2 }", 
            "\\Big[", "p^2", "C_{uu}", "+", "2p(1-p)", "C_{ud}", "+", "(1-p)^2", "C_{dd}", "\\Big]"  
        )

        formula_2.move_to(UP*1.5).scale(0.7)
        
        self.play(Write(formula_2))
        self.wait()

        
        text = TextMobject("$n$ Steps:")
        text.move_to(DOWN*1+LEFT*4)
        self.play(Write(text))
        
        formula_3 = TexMobject(
            "C", "=", "{1 \\over r^{n} }", 
            "\\Big[", "p^{n}", "C_{uu...u}", "+ \\cdots +", "{n \\choose j} p^j (1-p)^{n-j}", "C_{u...d}", "+ \\cdots +", "(1-p)^n", "C_{dd...d}", "\\Big]"  
        )

        formula_3.move_to(DOWN*2.5).scale(0.7)
        
        self.play(Write(formula_3))
        self.wait()

