from manimlib.imports import *

class a20200419(Scene):
    # def construct(self):
    #     grid = NumberPlane()
    #     self.play(FadeIn(grid))
    #     self.wait()

    def construct(self):
        for x in range(-7, 8):
            for y in range(-5, 6):
                annotation = TexMobject(f'P({x}, {y}, 0)', height=1.5, fill_opacity=.5)
                self.add(annotation)
                dot = Dot(point=(x, y, 0))
                self.add(dot)
                self.wait(.1)
                self.remove(annotation)
        