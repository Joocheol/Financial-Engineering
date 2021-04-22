from manimlib.imports import *

class test(Scene):
    def construct(self):
        self.get_vector_test()

    

    def get_vector_test(self):
        plane = NumberPlane()
        a = np.array([1,3,0])
        b = np.array([2,2,0])

        vector_a = Vector(a)
        vector_b = Vector(b)

        c = Arrow(a,b, buff=0)
        vector_c = Vector(c.get_vector())

        self.add(plane)
        self.add(vector_a, vector_b, c)
        self.play(ShowCreation(vector_c))

        self.wait()

    
