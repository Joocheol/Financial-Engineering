from manimlib.imports import *

class a20200513_03(GraphScene):
    
    CONFIG = {
        "y_max" : 1.2,
        "y_min" : 0,
        "x_min" : -3,
        "x_max" : 3,
        "x_axis_width": 7,
        "graph_origin": [2.5,-3,0]
    }


    def construct(self):
########
        string = r"""
            f(x) = {{1} \over {1 + e^{-x}}}
        """
        string = string.split()
        f_1 = TexMobject(*string)
        f_1.to_edge(UP, buff=0)

        self.play(Write(f_1))
        self.wait()

        string = r"""
            g_{x} (x, y) = {{e^{-x}} \over {e^{-x} + e^{-y}}} 
        """
        string = string.split()
        f_2 = TexMobject(*string)
        #f_2.next_to(f_1, DOWN, buff = 0.5)

        string = r""" 
            g_{y} (x, y) = {{e^{-y}} \over {e^{-x} + e^{-y}}}
        """
        string = string.split()
        f_3 = TexMobject(*string)
        #f_3.next_to(f_2, RIGHT, buff = 1)
        f_23 = VGroup(f_2, f_3).arrange_submobjects(RIGHT,buff=1,aligned_edge=DOWN)
        f_23.next_to(f_1, DOWN, buff=0.5)

        self.play(Write(f_23))
        self.wait()

        string = r"""
            g_{x} (0, y) = {{e^{-0}} \over {e^{-0} + e^{-y}}} = {{1} \over {1 + e^{-y}}}  
        """
        string = string.split()
        f_2_1 = TexMobject(*string)
        f_2_1.next_to(f_23, DOWN, buff=0.5)

        self.play(ReplacementTransform(f_2.copy(), f_2_1))
        self.wait()

        string = r"""
            g_{x} + g_{y} = {{e^{-x}} \over {e^{-x} + e^{-y}}} 
            + {{e^{-y}} \over {e^{-x} + e^{-y}}} = 1
        """
        string = string.split()
        f_2_2 = TexMobject(*string)
        f_2_2.next_to(f_2_1, DOWN, buff=0.5)

        self.play(Transform(f_23.copy(), f_2_2))
        self.wait()

        string = r"""
            g_{x} (x+a, y+a) = {{e^{-(x+a)}} \over {e^{-(x+a)} + e^{-(y+a)}}} 
            = {{e^{-x}} \over {e^{-x} + e^{-y}}}  
        """
        string = string.split()
        f_2_3 = TexMobject(*string)
        f_2_3.next_to(f_2_2, DOWN, buff=0.5)

        self.play(ReplacementTransform(f_2.copy(), f_2_3))
        self.wait()

        

        
########

    