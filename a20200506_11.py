from manimlib.imports import *

class a20200505_11(Scene):
    def construct(self):

        f_1 = TexMobject(
            "\\mathbb{E} (X) = \\sum",
            "^{n}", 
            "_{x",
            "=0}", 
            "x", 
            "{{n}", 
            "\\choose", 
            "{x}}",
            "p",
            "^x",
            "(1-p)",
            "^{n-",
            "x}"
        )
        [f_1[i].set_color(YELLOW) for i in (2,4,9,12)]
        f_1[6][1].set_color(YELLOW)
        self.play(Write(f_1))
        self.wait()
        self.play(Uncreate(f_1))

        f_1 = TexMobject(
            "\\mathbb{E} (X) = \\sum",
            "^{n}", 
            "_{i",
            "=0}", 
            "i", 
            "{{n}", 
            "\\choose", 
            "{i}}",
            "p",
            "^i",
            "(1-p)",
            "^{n-",
            "i}"
        )
        [f_1[i].set_color(BLUE) for i in (2,4,9,12)]
        f_1[6][1].set_color(BLUE)
        self.play(Write(f_1))
        self.wait()
        self.play(Uncreate(f_1))

        f_1 = TexMobject(
            "\\mathbb{E} (X) = \\sum",
            "^{n}", 
            "_{j",
            "=0}", 
            "j", 
            "{{n}", 
            "\\choose", 
            "{j}}",
            "p",
            "^j",
            "(1-p)",
            "^{n-",
            "j}"
        )
        [f_1[i].set_color(RED) for i in (2,4,9,12)]
        f_1[6][1].set_color(RED)
        self.play(Write(f_1))
        self.wait()
        self.play(Uncreate(f_1))

        f_1 = TexMobject(
            "\\mathbb{E} (X) = \\sum",
            "^{n}", 
            "_{k",
            "=0}", 
            "k", 
            "{{n}", 
            "\\choose", 
            "{k}}",
            "p",
            "^k",
            "(1-p)",
            "^{n-",
            "k}"
        )
        [f_1[i].set_color(PURPLE) for i in (2,4,9,12)]
        f_1[6][1].set_color(PURPLE)
        self.play(Write(f_1))
        self.wait()
