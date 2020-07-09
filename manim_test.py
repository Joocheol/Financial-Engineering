from manimlib.imports import *

class manim_test():

    print(color_to_rgba(Color('blue')))
    print(rgb_to_color(np.array([0,1,0])))
    print(random_bright_color())

    a = Mobject()
    print(a.dim)
    print(a.points)
    print(np.zeros((1,3)))