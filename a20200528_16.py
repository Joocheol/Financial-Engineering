from manimlib.imports import *

class a20200528_16(Scene):
    def construct(self):

        string = r""" \max (S_T - K, 0) - \max (K - S_T, 0) = S_T - K """
        string = string.split()
        text_1 = TexMobject(*string)
        string = r""" c - p = S_0 - K r^{-1} """
        string = string.split()
        text_2 = TexMobject(*string)
        g = VGroup(text_1, text_2).arrange_submobjects(DOWN, buff = 1)
        self.play(Write(g))
        self.wait(2)