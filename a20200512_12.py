from manimlib.imports import *

class a20200512_12(Scene):
    def construct(self):

        formula_4 = TexMobject(
            "C", "=", "{1 \\over r^{n} }", 
            "\\sum_{j=0}^{n}", "{n \\choose j}", "p^{j} (1-p)^{n-j}", "\\max ( u^{j} d^{n-j} S - K, 0)"
        )

        #formula_4.move_to(DOWN*2.5).scale(0.7)
        
        self.play(Write(formula_4))
        self.wait(5)
        