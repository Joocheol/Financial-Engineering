from manimlib.imports import *

class a20200507_10(GraphScene):
    
    CONFIG = {
        "y_max" : 1,
        "x_max" : 1,
        "axes_color" : BLUE,
    }

    def construct(self):

        self.setup_axes(animate=True)

        g = lambda x : 4 * x * (1-x)

        graph = self.get_graph(
            g, 
            color = GREEN
        )

        self.play(
            ShowCreation(graph),
        )
        self.wait(1)

        h = lambda x : x

        graph = self.get_graph(
            h, 
            color = RED
        )

        self.play(
            ShowCreation(graph),
        )
        self.wait(1)


        pt = Dot()
        # pt.move_to(self.coords_to_point(0.5, 0.3))
        # self.play(
        #     ShowCreation(pt),
        # )

        # #pt.move_to(self.coords_to_point(0.5, 0.5))
        # self.play(
        #     ApplyMethod(pt.move_to, self.coords_to_point(0.5, 0.5) )
        # )

        
        x = [0.1, 0.2, ]
        x = 0.3
        for i in range(30):
            
            self.play(ApplyMethod(pt.move_to, self.coords_to_point(x, g(x))))
            self.play(ApplyMethod(pt.move_to, self.coords_to_point(g(x,), g(x))))
            x = g(x)


        self.graph_origin = RIGHT*2 + UP*2
        self.setup_axes(animate=True)

        g = lambda x : 4 * x * (1-x)

        graph = self.get_graph(
            g, 
            color = GREEN
        )

        self.play(
            ShowCreation(graph),
        )
        self.wait(1)

        x = [0.1, 0.2, ]
        x = 0.3
        for i in range(30):
            
            self.play(ApplyMethod(pt.move_to, self.coords_to_point(x, g(x))))
            self.play(ApplyMethod(pt.move_to, self.coords_to_point(g(x,), g(x))))
            x = g(x)
