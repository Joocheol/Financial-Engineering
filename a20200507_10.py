from manimlib.imports import *

class a20200507_10(Scene):
    def construct(self):

        str = r"""
            \mathbb{E} (X) = {n\choose{k}}
        """
        str = str.split()
        f_1 = TexMobject(*str)
        f_1[1][0].set_color(RED)
        self.play(Write(f_1))
        self.wait()

        str = r"""
            {n\choose{k}}
        """
        str = str.split()
        f_2 = TexMobject(*str)
        f_2[0][1].set_color(RED)
        self.play(ApplyMethod(f_1.move_to, UP*1.5))
        self.play(Write(f_2))
        self.wait()

