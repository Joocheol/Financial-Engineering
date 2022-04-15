from manimlib.imports import *
from scipy.stats import binom

class a20200510_05(GraphScene):
    
    CONFIG = {
            "y_min" : 0,
            "y_max" : 0.3,
            "x_min" : 0,
            "x_max" : 31,
            "y_axis_label": "$\\mathbb{P} (X=x)$",
        }

    def construct(self):
        
        self.setup_axes(animate=True,)

        N = 10
        p = 0.2

        v_1 = self.plot_things(4,p)
        self.add(v_1)
        
        for N in range(5,31):
            v = self.plot_things(N, p)
            self.play(Transform(v_1, v))

        self.add(v_1)
        self.wait()

    def plot_things(self, N, p):

        string = "N = {}, p = {}".format(N,p)
        string = string.split()
        f_1 = Tex(*string)
        f_1.move_to(UP*3+RIGHT)

        things = VGroup()

        for i in range(N+1):
            thing = Dot()
            line = Line(start=[0,0.01,0], end=[0,0,0])
            line.set_length(self.coords_to_point(i, binom.pmf(i, n=N, p=p))[1] + 2.5)
            thing.move_to(self.coords_to_point(i, binom.pmf(i, n=N, p=p)))
            line.move_to(self.coords_to_point(i, binom.pmf(i, n=N, p=p)/2))
            things.add(thing, line)
        
        return VGroup(f_1, things)


        







