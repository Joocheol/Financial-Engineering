from manimlib.imports import *

class a20200507_05(Scene):
    def construct(self):
        str = r""" 
        \mathbb{E} (X) = \sum^{n}_{k=0} k {{n}\choose{k}} p^{k} (1-p)^{n-k}  
        """
        str = str.split()
        
        f_1 = TexMobject(*str)
        #f_1[3][2:5].set_color(RED)
        # f_1[13][:].set_color(RED)
        # f_1[14:16][:].set_color(YELLOW)
        # f_1[22:24][:].set_color(YELLOW)
        self.play(Write(f_1))
        self.wait()
        self.play(ApplyMethod(f_1[3][2:5].set_color, YELLOW))
        self.wait()

        str = r""" 
        \mathbb{E} (X) = \sum^{n}_{k=1} k {{n}\choose{k}} p^{k} (1-p)^{n-k}  
        """
        str = str.split()
        
        f_2 = TexMobject(*str)
        f_2[3][2:5].set_color(YELLOW)
        self.play(ReplacementTransform(f_1, f_2))
        self.wait()
        self.play(
            ApplyMethod(f_2[3][2:5].set_color, WHITE))
        self.wait()
        self.play(
            ApplyMethod(f_2[4:6].set_color, YELLOW))
        self.wait()

        str = r""" 
        \mathbb{E} (X) = \sum^{n}_{k=1} n {{n-1}\choose{k-1}} p^{k} (1-p)^{n-k}
        """
        str = str.split()
        
        f_3 = TexMobject(*str)
        f_3[4:6].set_color(YELLOW)
        self.play(ReplacementTransform(f_2, f_3))
        self.wait()
        self.play(
            ApplyMethod(f_3[4:6].set_color, WHITE))
        self.wait()
        self.play(
            ApplyMethod(f_3[4].set_color, YELLOW),
            ApplyMethod(f_3[6].set_color, YELLOW))
        self.wait()

        str = r""" 
        \mathbb{E} (X) = np \sum^{n}_{k=1} {{n-1}\choose{k-1}} p^{k-1} (1-p)^{n-k}
        """
        str = str.split()
        
        f_4 = TexMobject(*str)
        f_4[3].set_color(YELLOW)
        f_4[6].set_color(YELLOW)
        self.play(ReplacementTransform(f_3, f_4))
        self.wait()
        self.play(
            ApplyMethod(f_4[3].set_color, WHITE),
            ApplyMethod(f_4[6].set_color, WHITE))
        self.wait()
        self.play(
            ApplyMethod(f_4[7][5:8].set_color, YELLOW))
        self.wait()

        str = r""" 
        \mathbb{E} (X) = np \sum^{n}_{k=1} {{n-1}\choose{k-1}} p^{k-1} (1-p)^{(n-1)-(k-1)}
        """
        str = str.split()
        
        f_5 = TexMobject(*str)
        f_5[7][5:].set_color(YELLOW)
        self.play(ReplacementTransform(f_4, f_5))
        self.wait()
        self.play(
            ApplyMethod(f_5[7].set_color, WHITE),)
        self.wait()

        str = r""" k = 1, 2, \cdots , n"""
        str = str.split()
        
        f_6 = TexMobject(*str)
        f_6.move_to(DOWN*1.5)
        self.play(Write(f_6))
        self.wait()

        str = r""" k-1 = 0, 1, \cdots , n-1"""
        str = str.split()
        
        f_7 = TexMobject(*str)
        f_7.move_to(DOWN*2.5)
        self.play(Write(f_7))
        self.wait()

        str = r""" j = 0, 1, \cdots , m"""
        str = str.split()
        
        f_8 = TexMobject(*str)
        f_8.move_to(DOWN*2.5)
        self.play(ReplacementTransform(f_7, f_8))
        self.wait()

        self.play(
            ApplyMethod(f_5[4][0].set_color, YELLOW),
            ApplyMethod(f_5[4][2:].set_color, YELLOW),
            ApplyMethod(f_5[5][1:7].set_color, YELLOW),
            ApplyMethod(f_5[6][1:].set_color, YELLOW),
            ApplyMethod(f_5[7][6:9].set_color, YELLOW),
            ApplyMethod(f_5[7][12:15].set_color, YELLOW),
        )
        self.wait()


        
        



        
        # str = str.split()
        # f_1 = TexMobject(*str)
        # f_1[4][:].set_color(RED)
        # f_1[6][0].set_color(RED)
        # f_1[6][1].set_color(YELLOW)
        # f_1[7][5:8].set_color(YELLOW)
        # f_1[9:11][:].set_color(RED)
        # f_1[15][1:].set_color(YELLOW)
        # f_1[16][5:].set_color(YELLOW)
        # self.play(Write(f_1))
        # self.wait()

        # &= \\sum ^{n} _{k=1} k {n\\choose{k}} p^{k} (1-p)^{n-k}\\\ 
        # &= \\\ 

        # &= n p \\sum ^{n} _{k=1} {{n-1}\\choose{k-1}} p^{k-1} (1-p)^{(n-1)-(k-1)}\\\  
        # &= n p \\sum ^{m} _{j=0}  {{m}\\choose{j}} p^{j} (1-p)^{m-j} = n p