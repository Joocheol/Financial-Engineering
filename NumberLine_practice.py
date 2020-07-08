from manimlib.imports import *

class NumberLine_practice(Scene):
    def construct(self):

        n_line = NumberLine(
            x_min=-5,  x_max=5,
            unit_size=0.5,
            include_numbers=True,
            tick_frequency=1,
        )
        self.play(Write(n_line))
        path =  ArcBetweenPoints(LEFT*4+UP*2, RIGHT*4 + DOWN*2, angle=-PI/2, stroke_width=8)

        self.play(MoveAlongPath(n_line, path), run_time=3)
        self.wait()