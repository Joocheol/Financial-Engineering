from manimlib.imports import *

class n_step(Scene):
    def construct(self):

        text = TextMobject("1 Step:")
        text.move_to(UP*3+LEFT*4)
        self.play(Write(text))

        formula_1 = Tex(
            "C", "=", "{1 \\over r }", 
            "\\Big[", "p", "C_{u}", "+", "(1-p)", "C_{d}", "\\Big]"  
        )

        formula_1.move_to(UP*2.5).scale(0.7)
        
        self.play(Write(formula_1))
        self.wait(3)

        text = TextMobject("2 Steps:")
        text.move_to(UP*2+LEFT*4)
        self.play(Write(text))
        
        formula_2 = Tex(
            "C", "=", "{1 \\over r^2 }", 
            "\\Big[", "p^2", "C_{uu}", "+", "2p(1-p)", "C_{ud}", "+", "(1-p)^2", "C_{dd}", "\\Big]"  
        )

        formula_2.move_to(UP*1).scale(0.7)
        
        self.play(Write(formula_2))
        self.wait(3)

        
        text = TextMobject("$n$ Steps:")
        text.move_to(DOWN*0+LEFT*4)
        self.play(Write(text))
        
        formula_3 = Tex(
            "C", "=", "{1 \\over r^{n} }", 
            "\\sum_{j=0}^{n}", "{n \\choose j}", "p^{j} (1-p)^{n-j}", "C_{uu...dd}"
        )

        formula_3.move_to(DOWN*1).scale(0.7)
        
        self.play(Write(formula_3))
        self.wait(3)

        formula_4 = Tex(
            "C", "=", "{1 \\over r^{n} }", 
            "\\sum_{j=0}^{n}", "{n \\choose j}", "p^{j} (1-p)^{n-j}", "\\max ( u^{j} d^{n-j} S - K, 0)"
        )

        formula_4.move_to(DOWN*2.5).scale(0.7)
        
        self.play(Write(formula_4))
        for i in range(3):
            self.play(Transform(formula_3[6].copy(), formula_4[6]))
        self.wait(3)

