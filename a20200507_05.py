from manimlib.imports import *

class a20200507_05(Scene):
    def construct(self):
        str = """ 
        \\mathbb{E} (X) &= \\sum ^{n} _{k=0} k {n\\choose{k}} p^{k} (1-p)^{n-k}\\\  
        &= \\sum ^{n} _{k=1} k {n\\choose{k}} p^{k} (1-p)^{n-k}\\\ 
        &= \\sum ^{n} _{k=1} n {{n-1}\\choose{k-1}} p^{k} (1-p)^{n-k}\\\ 
        """
        str_s = str.split()
        f_1 = TexMobject(*str_s)
        f_1[5][:].set_color(RED)
        f_1[13][:].set_color(RED)
        f_1[14:16][:].set_color(YELLOW)
        f_1[22:24][:].set_color(YELLOW)
        self.play(Write(f_1))
        self.wait()
        self.play(FadeOut(f_1))

        str = """ 
        &= \\sum ^{n} _{k=1} n {{n-1}\\choose{k-1}} p^{k} (1-p)^{n-k}\\\ 
        &= n p \\sum ^{n} _{k=1} {{n-1}\\choose{k-1}} p^{k-1} (1-p)^{(n-1)-(k-1)}\\\  
        &= n p \\sum ^{m} _{j=0}  {{m}\\choose{j}} p^{j} (1-p)^{m-j} = n p
        """
        str_s = str.split()
        f_1 = TexMobject(*str_s)
        f_1[4][:].set_color(RED)
        f_1[6][0].set_color(RED)
        f_1[6][1].set_color(YELLOW)
        f_1[7][5:8].set_color(YELLOW)
        f_1[9:11][:].set_color(RED)
        f_1[15][1:].set_color(YELLOW)
        f_1[16][5:].set_color(YELLOW)
        self.play(Write(f_1))
        self.wait()