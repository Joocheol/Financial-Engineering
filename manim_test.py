from manimlib.imports import *

class manim_test(Scene):
    def construct(self):

        # a = Circle(color=YELLOW)
        # a.point_at_angle(0.3)
        # self.play(ShowCreation(a))

        b = Arc(num_components=4)
        self.play(ShowCreation(b))
        print(b.points)

        
