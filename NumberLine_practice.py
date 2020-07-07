from manimlib.imports import *

class NumberLine_practice(Scene):
    def construct(self):

        n_line = NumberLine(
            x_min=-5,  x_max=5,
            unit_size=0.5,
            include_numbers=True,
            tick_frequency=1,
        )
        self.add(n_line)
        self.wait()