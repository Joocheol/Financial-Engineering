from manimlib.imports import *

class a20200517_14(Scene):
    def construct(self):


        t_x = TexMobject(r"""
            \texttt{x = [6,7,8,9]}
            """)
        t_y = TexMobject(r"""
            \texttt{y = [10,20,30,40]}
            """)

        t = VGroup(t_x, t_y).arrange_submobjects(DOWN, buff=0.5)
        self.play(ShowCreation(t))
        self.wait()
        
        code_x = TexMobject(r"""
            \texttt{x = [6,7,8,9]} 
            """)
        code_y = TexMobject(r"""
            \texttt{y = [10,20,30,40]} 
            """)
        #code_xy_g.scale(0.7).next_to(t_1, DOWN, aligned_edge=LEFT, buff=0)

        #code_xy_g[0][3].set_color(YELLOW)

        code_xy_g = VGroup(code_x,code_y).arrange_submobjects(DOWN,aligned_edge=LEFT,buff=0).scale(0.7).move_to([-5,2,0])
        
        self.play(ReplacementTransform(t, code_xy_g))

        

        layer_1_code = TexMobject(r"""
            \texttt{Dense(1, input\textunderscore shape=[1])}
            """)
        layer_1_code.scale(0.7).next_to(code_xy_g, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(ShowCreation(layer_1_code))

        c = Circle(radius=0.1)
        c.move_to([2,0,0])

        self.play(ReplacementTransform(layer_1_code.copy(),c))
        self.wait()
###

        t_3 = TexMobject(r"""
            \texttt{6} 
            """)
        t_3.move_to([2,3,0]).scale(0.7)
        

        t_4 = TexMobject(r"""
            \texttt{10} 
            """)
        t_4.move_to([2,-3,0]).scale(0.7)

        self.play(ReplacementTransform(t_x[0][3].copy(), t_3))
        self.play(ReplacementTransform(t_y[0][3:5].copy(), t_4))

###

        layer_1_f = TexMobject(r"""
            w\cdot[\quad] + b
            """)

        layer_1_f.move_to([2,0,0])

        self.play(ReplacementTransform(c, layer_1_f))
        self.wait()

###
        self.play(Uncreate(layer_1_code))
        self.play(FadeOut(layer_1_f))
        self.wait()

        layer_1_code = TexMobject(r"""
            \texttt{Dense(2, input\textunderscore shape=[1])}
            """)
        layer_1_code.scale(0.7).next_to(code_xy_g, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(layer_1_code))

        c_2 = Circle(radius=0.1)
        c_3 = Circle(radius=0.1)
        c_g = VGroup(c_2,c_3)
        c_g.arrange_submobjects(RIGHT, buff=1)
        c_g.move_to([2,0,0])


        self.play(ReplacementTransform(layer_1_code.copy(),c_g))
        self.wait()

###

        f_2 = TexMobject(r"""
            w_{1}\cdot[\quad] + b_{1}
            """)
        f_3 = TexMobject(r"""
            w_{2}\cdot[\quad] + b_{2}
            """)

        f_g = VGroup(f_2,f_3).arrange_submobjects(RIGHT, buff=1,).scale(0.7).move_to([2,0,0])

        self.play(ReplacementTransform(c_g,f_g))
        self.wait()

###
        
        layer_2_code = TexMobject(r"""
            \texttt{Dense(1)}
            """)
        layer_2_code.scale(0.7).next_to(layer_1_code,DOWN,aligned_edge=LEFT,buff=0)

        self.play(Write(layer_2_code))
        self.wait()

        self.play(FadeOut(f_g))
        self.wait()

        c_4 = Circle(radius=0.1)
        c_5 = Circle(radius=0.1)
        c_6 = Circle(radius=0.1)
        c = VGroup(c_4,c_5).arrange_submobjects(RIGHT, buff=1,)
        c = VGroup(c,c_6).arrange_submobjects(DOWN, buff=1).move_to([2,0,0])

        self.play(ReplacementTransform(layer_2_code.copy(), c))
        self.wait()

        layer_2_f_1 = TexMobject(r"""
            w_{11}\cdot[\quad] + b_{11}
        """)
        layer_2_f_2 = TexMobject(r"""
            w_{12}\cdot[\quad] + b_{12}
        """)
        layer_2_f_3 = TexMobject(r"""
            w_{21}\cdot[\quad] + w_{21}\cdot[\quad] + b_{21}
        """)

        layer_2_g = VGroup(layer_2_f_1, layer_2_f_2).arrange_submobjects(RIGHT, buff=1)
        layer_2_g = VGroup(layer_2_g, layer_2_f_3).arrange_submobjects(DOWN,buff=1).scale(0.7).move_to([2,0,0])

        self.play(ReplacementTransform(c,layer_2_g))
        self.wait()


        
















