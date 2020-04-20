from manimlib.imports import *

class a20200420(Scene):
    def construct(self):

        formula_1 = TexMobject(
            "C_u", "=", "{1 \\over r}", "\\Big[", "p", "C_{uu}", "+", "(1-p)", "C_{ud}", "\\Big]"
        )
        
        formula_1.move_to(UP*2.5)
        
        self.play(Write(formula_1))
        self.wait()
        
        formula_2 = TexMobject(
            "C_d", "=", "{1 \\over r}", "\\Big[", "p", "C_{ud}", "+", "(1-p)", "C_{dd}", "\\Big]"  
        )

        formula_2.move_to(UP)
        
        self.play(Write(formula_2))
        self.wait()
        
        formula_3 = TexMobject(
            "C", "=", "{1 \\over r}", "\\Big[", "p", "C_{u}", "+", "(1-p)", "C_{d}", "\\Big]"  
        )

        formula_3.move_to(DOWN)
        
        self.play(Write(formula_3))
        self.wait()

        self.play(Transform(formula_1.copy(), formula_3[5]))
        self.wait()
        self.play(Transform(formula_2.copy(), formula_3[8]))
        self.wait()

        formula_4 = TexMobject(
            "", "=", "{1 \\over r^2 }", "\\Big[", "p^2", "C_{uu}", "+", "2p(1-p)", "C_{ud}", "+", 
            "(1-p)^2", "C_{dd}", "\\Big]"  
        )

        formula_4.move_to(DOWN*2.5)
        
        self.play(Write(formula_4))
        self.wait()
