from manimlib.imports import *

class Python_01(Scene):
    def construct(self):

        code_01 = TextMobject(r'''
            \begin{verbatim} 
            x = 3
            print(x)
            print(type(x))
            x = 3
            print(x)
            print(type(x))
            \end{verbatim}
        ''')
        self.play(Write(code_01))
