from manimlib.imports import *

class a20200507_10(GraphScene):
    
    CONFIG = {
        "y_max" : 10,
        "x_max" : 14,
        "axes_color" : BLUE
    }

    def construct(self):

        self.setup_axes(animate=True)

        # graph = self.get_graph(
        #     lambda x : np.sin(x), 
        #     color = GREEN
        # )

        # self.play(
        #     ShowCreation(graph),
        # )
        # self.wait(1)


        pt = Dot()

        g = lambda x : 4 * x * (1-x)
        #x = [0.1, 0.2, ]
        #g_x = [g(x) for x in  ]
        x = 0.3
        for i in range(10):
            
            self.play(ApplyMethod(pt.move_to, [x, g(x), 0]))
            self.play(ApplyMethod(pt.move_to, [g(x), g(x), 0]))
            x = g(x)
                
