from manimlib.imports import *


class test(Scene):
    def construct(self):
        grid = NumberPlane()
        self.play(ShowCreation(grid))
        self.wait()
        