from manimlib.imports import *

class a20200624(VectorScene):

    CONFIG = {
       "basis_vector_stroke_width": 6
    }

    def construct(self):

        grid = self.add_plane()
        #self.play(ShowCreation(grid))
        #self.wait()

    #    self.lock_in_faded_grid()
        #self.add_axes()
        #self.lock_in_faded_grid()
        #self.add_vector([1,2])
        #v = Vector([0,1])
        #self.write_vector_coordinates(v)
        #self.coords_to_vector([1,2])
    #    self.vector_to_coords([1,3])

        #plane = NumberPlane()
        #self.add(plane)
        #self.wait()

        self.add_vector([2,1], color=BLUE)

    def add_plane(self, animate=False, **kwargs):
        plane = NumberPlane(**kwargs)
        if animate:
            self.play(ShowCreation(plane, lag_ratio=0.5))
        self.add(plane)
        return plane


