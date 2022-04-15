from manimlib.imports import *

class a20200506_13(Scene):
    def construct(self):

        f_1 = Tex(
            "{n \\choose k} &= { {n!} \\over {k! (n-k)!} } \\\ ",
            "&= {", 
            " n ", 
            "\\times (n-1) \\times \\cdots \\times 1 \\over { [ ",
            "k", 
            " \\times (k-1) \\cdots 1] \\times  [(n-k) \\cdots 1] } } \\\ ",
            "&= { ",
            "n",
            " \\over ",
            "k } ",
            "{ (n-1) \\times \\cdots \\times 1 \\over [ (k-1) \\times \\cdots \\times 1 ] [ (n-k) \\cdots 1 ] }\\\ ",
            "& = { ",
            "n ",
            "\\over",
            "k }",
            "\\times { {n-1} \\choose {k-1} }")
        [f_1[i].set_color(YELLOW) for i in (2, 4, 7, 9, 12, 14)]
        self.play(Write(f_1))
        self.wait()