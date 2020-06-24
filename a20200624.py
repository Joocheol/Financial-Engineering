from manimlib.imports import *

class a20200624(VectorScene):

    CONFIG = {
        "basis_vector_stroke_width": 6
    }

    def construct(self):

        #grid = self.add_plane()
        #self.play(ShowCreation(grid))
        #self.wait()

        self.add_plane()
        #self.add_axes()
        #self.lock_in_faded_grid()
        self.add_vector([1,2])
        #v = Vector([0,1])
        #self.write_vector_coordinates(v)
        self.coords_to_vector([1,2])
