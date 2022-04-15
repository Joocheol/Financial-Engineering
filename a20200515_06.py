from manimlib.imports import *

class a20200515_06(Scene):
    def construct(self):
#
        string = r"""
            \Big( 1 + {1 \over 100}\Big)^{100} 
             &= 1 + {100 \choose 1} \Big( {1 \over 100} \Big)
             + {100 \choose 2} \Big( {1 \over 100} \Big)^2 \\&+ 
             + \cdots 
             + {n \choose j} \Big( {1 \over n} \Big)^j + \cdots
             + \Big( {1 \over n} \Big)^n   
        """.split()
        f_1 = Tex(*string)

        F = VGroup(f_1)
        F.arrange_submobjects(DOWN, buff=0.5)
        self.play(Write(F[:]))
        self.wait()