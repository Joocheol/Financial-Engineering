from manimlib.imports import *
from scipy.stats import binom

class a20200509_12(GraphScene):
    
    CONFIG = {
            "y_min" : 0,
            "y_max" : 0.3,
            "x_min" : 0,
            "x_max" : 30,
            "y_axis_label": "$\\mathbb{P} (X=x)$",
        }

    def construct(self):
        
        self.setup_axes(animate=True,)

        N = 10
        p = 0.6

        for N in range(5,30):
            self.plot_things(N, p)

    def plot_things(self, N, p):

        things=VGroup()

        for i in range(N+1):
            thing = Dot()
            thing.move_to(self.coords_to_point(i, binom.pmf(i, n=N, p=p)))
            things.add(thing)
        
        #things_g = VGroup(*things)
        self.add(things)
        #self.wait()
        self.play(FadeOut(things))


        







