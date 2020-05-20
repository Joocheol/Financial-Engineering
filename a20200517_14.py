from manimlib.imports import *

class a20200517_14(Scene):
    def construct(self):

        # c = Circle(radius=0.1)
        # c.move_to([0,0,0])

        # self.play(ShowCreation(c))
        #self.wait()

        t_x = TexMobject(r"""
            \texttt{x = [6,7,8,9]}
            """)
        #t_1.to_edge(LEFT+UP, buff=1)

        t_y = TexMobject(r"""
            \texttt{y = [11,21,31,41]}
            """)

        t = VGroup(t_x, t_y)
        t.arrange_submobjects(DOWN, buff=0.5)
        self.play(ShowCreation(t))
        self.wait()
        
        t_1 = TexMobject(r"""
            \texttt{x = [6,7,8,9]} 
            """)
        t_1.move_to([-5.5,2,0]).scale(0.7)
        

        t_2 = TexMobject(r"""
            \texttt{y = [10,20,30,40]} 
            """)
        t_2.scale(0.7).next_to(t_1, DOWN, aligned_edge=LEFT, buff=0)

        #t_2[0][3].set_color(YELLOW)
        
        self.play(Transform(t_x, t_1), 
            Transform(t_y, t_2)
            )

        

        t_5 = TexMobject(r"""
            \texttt{Dense(1, input\textunderscore shape=[1])}
            """)
        t_5.scale(0.7).next_to(t_2, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(ShowCreation(t_5))

        c = Circle(radius=0.1)
        c.move_to([2,0,0])

        self.play(ShowCreation(c))
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

        self.play(Transform(t_x[0][3].copy(), t_3))
        self.play(Transform(t_y[0][3:5].copy(), t_4))

###

        e_1=Ellipse(width=3, height=2)
        e_1.move_to([2,0,0])

        self.play(Transform(c, e_1))
        self.wait()

        f_1 = TexMobject(r"""
            w\cdot[\quad] + b
            """)

        f_1.move_to([2,0,0])

        self.play(Write(f_1))
        self.wait()
        c = VGroup(c,f_1)

###

        t_6 = TexMobject(r"""
            \texttt{Dense(2, input\textunderscore shape=[1])}
            """)
        t_6.scale(0.7).next_to(t_2, DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Transform(t_5,t_6))

        c_2 = Circle(radius=0.1)
        c_3 = Circle(radius=0.1)
        c_g = VGroup(c_2,c_3)
        c_g.arrange_submobjects(RIGHT, buff=1)
        c_g.move_to([2,0,0])


        self.play(Transform(c,c_g))
        self.wait()

###

        e_2=Ellipse(width=3, height=2)
        e_3=Ellipse(width=3, height=2)
        e_g = VGroup(e_2,e_3)
        e_g.arrange_submobjects(RIGHT, buff=0.5)
        e_g.move_to([2,0,0])

        self.play(Transform(c, e_g))
        self.wait()

        f_2 = TexMobject(r"""
            w_{1}\cdot[\quad] + b_{1}
            """)

        f_2.move_to([0.3,0,0]).scale(0.7)

        f_3 = TexMobject(r"""
            w_{2}\cdot[\quad] + b_{2}
            """)

        f_3.move_to([3.7,0,0]).scale(0.7)

        f_g = VGroup(f_2,f_3)

        self.play(Write(f_g))
        self.wait()
        
















