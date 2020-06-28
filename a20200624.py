from manimlib.imports import *

class a20200624(VectorScene):

    CONFIG = {
       "basis_vector_stroke_width": 6
    }

    def construct(self):

        plane = self.add_plane(animate=True)

        b = self.get_basis_vectors()
       

        a = self.add_vector([4,2])

        
        

        self.label_vector(a, [10,2], at_tip=True)

        self.add_vector(b[0])
        self.add_vector(b[1])

        self.label_vector(b[0], [1,1])

        self.vector_to_coords([-3,2])

        

    
    

