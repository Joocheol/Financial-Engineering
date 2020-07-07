from manimlib.imports import *

class a2020070710(Scene):
    def construct(self):

        self.add(NumberPlane())

        func1 = lambda x: x ** 5 -2 * x**2
        graph1 = FunctionGraph(
            func1,
            x_min=-4,
            x_max=3,
            color=YELLOW,
        )
        self.play(ShowCreation(graph1))
        self.wait()