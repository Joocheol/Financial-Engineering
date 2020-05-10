from manimlib.imports import *
import numpy as np

class a20200510_12(GraphScene):
    
    CONFIG = {
            "y_min" : 0,
            "y_max" : 10,
            "x_min" : -3,
            "x_max" : 7,
            "y_axis_label": "$y$",
        }

    def construct(self):
        
        self.setup_axes(animate=True,)

        g = lambda x : (x-1)**2 + 2

        graph_g = self.get_graph(g)
        self.play(ShowCreation(graph_g))



        formula = TexMobject("")
        formula.to_edge(RIGHT, buff = 1)
        self.add(formula)

        for w in range(-3,3):
            for b in range(-5,3):

                formula_1 = "\\max ( {} x + {}, 0 ) ".format(w,b)
                formula_1 = TexMobject(formula_1)
                formula_1.to_edge(RIGHT, buff = 1)
                
                f = lambda x : max(w*x + b, 0)
                graph_f = self.get_graph(f)
                
                self.play(
                    ShowCreation(graph_f),
                    Transform(formula, formula_1))


        # f_1 = lambda x : max(w*x + a[1], 0)
        # f_2 = lambda x : max(-a[2]*x + a[3], 0)
        # f_3 = lambda x : max((f_1(x) + f_2(x)) , 0)


        # g_g = self.get_graph(g)
        # graph_1 = self.get_graph(
        #     f_1
        # )
        # graph_2 = self.get_graph(
        #     f_2
        # )
        # graph_3 = self.get_graph(
        #     f_3,
        # )

        # self.play(
        #     ShowCreation(g_g),
        #     ShowCreation(graph_1),
        #     ShowCreation(graph_2),
        #     ShowCreation(graph_3),
        # )
        # self.wait(1)


        







