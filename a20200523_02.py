from manimlib.imports import *

class a20200523_02(Scene):
    def construct(self):

        things = setup()
        things.scale(0.7)

        self.play(ShowCreation(things))

        things2 = setup()
        things2.scale(0.2).to_edge(UL,)
        self.play(Transform(things, things2))

        self.play(Restore(things))
        


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
    CC_u = TexMobject("C_u")
    CC_d = TexMobject("C_d")

    tmp = VGroup(CC_u, CC_d).arrange_submobjects(DOWN, buff=1)
    C = VGroup(CC, tmp).arrange_submobjects(RIGHT, buff=1)

    things = VGroup(S, r, C).arrange_submobjects(RIGHT, buff=2)

    return things
