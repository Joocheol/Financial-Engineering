from manimlib.imports import *

class a20200424(Scene):
    def construct(self):

        a = Rectangle()
        #a.stoke_color=YELLOW
        #self.play(DrawBorderThenFill(a), Write(a.copy().move_to(DOWN)), run_time  = 10, stoke_color="GRAY")
        self.play(Indicate(a), point_color=BLUE)