from manimlib.imports import *

class a20200504_1(Scene):
    CONFIG = {
        "n_of_steps" : 20,
        "width" : 7,
        "height" : 5,
        "radius" : 0.1,
        "origin" : np.array([-4, 0, 0])
    }

    def construct(self):

        for i in [1, 2, 5, 10, 20]:
            self.my_tree(i)
            self.wait()

        
    def my_tree(self, steps):
        nodes = [
            [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
        ]
        
        for i in range(steps+1):
            for j in range(i+1): 
                location = self.origin \
                    + np.array([self.width/steps * i, 0, 0])  \
                    + np.array([0, self.height/steps * (j-i/2), 0])
                nodes[i][j].move_to(location)
            
        nodes_g = VGroup(*[nodes[i][j] for i in range(steps+1) for j in range(i+1)]) 

        self.play(ShowCreation(nodes_g))
        self.wait()