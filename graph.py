from manimlib.imports import *

class Graph(GraphScene):
    
    CONFIG = {
        "y_max" : 100,
        "axes_color" : BLUE
    }

    def construct(self):

    	self.setup_axes(animate=True)

    	graph = self.get_graph(
    		lambda x : np.sin(x), 
    		color = GREEN
    	)

    	self.play(
    		ShowCreation(graph),
    	)
    	self.wait(1)
