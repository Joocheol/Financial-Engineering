from manimlib.imports import *

class manim_test(Scene):
    def construct(self):

        a = Dot()
        b = TextMobject("Hello")
        a.surround(b)
        self.play(ShowCreation(b))
        self.play(ShowCreation(a))

        c = Circle()
        c.add_tip()
        self.play(ShowCreation(c))

        print(a.points)
        print(b.points)
        print(c.points)