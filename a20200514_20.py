from manimlib.imports import *

class a20200514_20(Scene):
    def construct(self):
#1
        string = r"""
            \Big( 1 + {1 \over n}\Big)^n    
        """.split()
        f_1 = Tex(*string)
        #f_1.to_edge(UL, buff=0.5)

        string = r"""
            \Big( 1 + {1 \over n}\Big)^2 = 1 + 2 \Big( {1 \over n} \Big) + \Big( {1 \over n} \Big)^2  
        """.split()
        f_2 = Tex(*string)

        string = r"""
            \Big( 1 + {1 \over n}\Big)^3 
             = 1 + 3 \Big( {1 \over n} \Big) + 3 \Big( {1 \over n} \Big)^2 + \Big( {1 \over n} \Big)^3 
        """.split()
        f_3 = Tex(*string)

        string = r"""
            \vdots
        """.split()
        f_4 = Tex(*string)

        string = r"""
            \Big( 1 + {1 \over n}\Big)^n 
             = 1 + {n \choose 1} \Big( {1 \over n} \Big) + \cdots 
             + {n \choose j} \Big( {1 \over n} \Big)^j + \cdots
             + \Big( {1 \over n} \Big)^n   
        """.split()
        f_5 = Tex(*string)

        F = VGroup(f_1, f_2, f_3, f_4, f_5)
        F.arrange_submobjects(DOWN, buff=0.5)
        self.play(Write(F[:]))
        self.wait()
        self.play(FadeOut(F))
