from manimlib.imports import *

class a20200624(VectorScene):

    CONFIG = {
        "basis_vector_stroke_width": 6
    }

    def construct(self):

        grid = self.add_plane()
        self.play(ShowCreation(grid))
        self.wait()
