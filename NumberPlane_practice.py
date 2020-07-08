from manimlib.imports import *

class NumberPlane_practice(Scene):
    def construct(self):

        
        v_1 = Vector([-2,1])
        v_2 = Vector()

        
        self.add(v_1)
        self.add(v_2)

        text = TextMobject("Vector Space")
        self.play(Write(text))

        self.add_plane()
        self.wait()


    def add_plane(self):
        plane = NumberPlane()
        #self.play(ShowCreation(plane))
        self.add(plane)
        return plane