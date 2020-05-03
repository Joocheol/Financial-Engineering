from manimlib.imports import *

class Tree(Scene):
    CONFIG = {
        "n_of_steps" : 100,
        "width" : 7,
        "height" : 5,
        "radius" : 0.1,
        "origin" : np.array([-4, 0, 0])
    }
    
    def construct(self):

        nodes = [
            [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
        ]
        
        for i in range(self.n_of_steps+1):
            for j in range(i+1): 
                location = self.origin \
                    + np.array([self.width/self.n_of_steps * i, 0, 0])  \
                    + np.array([0, self.height/self.n_of_steps * (j-i/2), 0])
                self.play(Write(nodes[i][j].move_to(location)), run_time = 0.1)

