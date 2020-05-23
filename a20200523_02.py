from manimlib.imports import *

class a20200523_02(Scene):
    def construct(self):

        title = title_1_setup()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        things = setup()
        things.scale(0.7)
        self.play(ShowCreation(things))
        self.wait()

        things2 = setup()
        things2.scale(0.2).to_edge(UL,)
        self.play(Transform(things, things2))

        title = title_2_setup()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        title = title_3_setup()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        title = title_4_setup()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        title = title_5_setup()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        title = title_6_setup()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

def title_6_setup():
    text = TexMobject(r"""C - P &= {1 \over r} \Big[ p [ C_u - P_u ] + (1-p) [ C_d - P_d ] \Big] """)
    return text

def title_5_setup():
    text = TexMobject(r"""C &= {1 \over r} \Big[ p C_u + (1-p) C_d \Big] \\ 
        - P &= {1 \over r} \Big[ p P_u + (1-p) P_d \Big] """)
    return text

def title_4_setup():
    text = TextMobject("Can you calculate $C - P$? ")
    return text


def title_3_setup():
    text = TexMobject(r"P = {1 \over r} \Big[ p P_u + (1-p) P_d \Big] ")
    return text
        
def title_2_setup():
    text = TextMobject("We know how to solve this problem")
    return text
    
def title_1_setup():
    text = TextMobject("Revisiting the games with the put option")
    return text



def setup():

    SS = TexMobject("S")
    SS_u = TexMobject("u S")
    SS_d = TexMobject("d S")

    tmp = VGroup(SS_u, SS_d).arrange_submobjects(DOWN, buff=1)
    S = VGroup(SS, tmp).arrange_submobjects(RIGHT, buff=1)

    rr = TexMobject("1")
    rr_u = TexMobject("r")
    rr_d = TexMobject("r")

    tmp = VGroup(rr_u, rr_d).arrange_submobjects(DOWN, buff=1)
    r = VGroup(rr, tmp).arrange_submobjects(RIGHT, buff=1)

    CC = TexMobject("?")
    CC_u = TexMobject("P_u")
    CC_d = TexMobject("P_d")

    tmp = VGroup(CC_u, CC_d).arrange_submobjects(DOWN, buff=1)
    C = VGroup(CC, tmp).arrange_submobjects(RIGHT, buff=1)

    things = VGroup(S, r, C).arrange_submobjects(RIGHT, buff=2)

    return things
