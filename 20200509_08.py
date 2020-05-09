from manimlib.imports import *

class a20200509_08(Scene):
    def construct(self):

        str = r"""
            C = {1 \over r} \sum^{n}_{j=0} {{n}\choose{j}} p^{j} (1-p)^{n-j} 
            \max [ u^{j} d^{n-j} S - K , 0 ] 
        """
        str = str.split()
        f_1 = TexMobject(*str)
        f_1.scale(0.7)
        self.play(Write(f_1))
        self.wait() 

        str = r"""
             = {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j} 
            ( u^{j} d^{n-j} S - K ) 
        """
        str = str.split()
        f_2 = TexMobject(*str)
        f_2.scale(0.7)
        self.play(ApplyMethod(f_1.shift, UP*1.2))
        self.play(Write(f_2))
        self.wait() 

        str = r"""
             = S {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j} u^{j} d^{n-j} 
             - K {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j} 
        """
        str = str.split()
        f_3 = TexMobject(*str)
        f_3.scale(0.7)
        self.play(ApplyMethod(f_1.shift, UP*1.2), ApplyMethod(f_2.shift, UP*1.2))
        self.play(Write(f_3))
        self.wait() 

        str = r"""
             = S {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} [ p u ]^{j} [ (1-p) d ]^{n-j} 
             - K {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j} 
        """
        str = str.split()
        f_4 = TexMobject(*str)
        f_4.scale(0.7)

        self.play(Write(f_4.shift(DOWN*1.2)))
        self.wait() 

        str = r"""
             = S \sum^{n}_{j=a} {{n}\choose{j}} 
             \Big[ {p u \over r} \Big]^{j} \Big[ {(1-p) d \over r} \Big]^{n-j} 
             - K {1 \over r} \sum^{n}_{j=a} {{n}\choose{j}} p^{j} (1-p)^{n-j} 
        """
        str = str.split()
        f_5 = TexMobject(*str)
        f_5.scale(0.7)

        self.play(Write(f_5.shift(DOWN*2.4)))
        self.wait() 