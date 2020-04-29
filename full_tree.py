from manimlib.imports import *

class full_tree(Scene):
    def construct(self):

        node_0_0 = TexMobject("S")
        node_1_0 = TexMobject("d S")
        node_1_1 = TexMobject("u S")
        node_2_0 = TexMobject("d^2 S")
        node_2_1 = TexMobject("ud S")
        node_2_2 = TexMobject("u^2 S")
        # node_3_0 = TexMobject("\\ddots")
        # node_3_1 = TexMobject("")
        # node_3_2 = TexMobject("")
        # node_3_3 = TexMobject("\\iddots")
        node_4_0 = TexMobject("d^n S")
        node_4_1 = TexMobject("\\vdots")
        node_4_2 = TexMobject("u^j d^{n-j} S")
        node_4_3 = TexMobject("\\vdots")
        node_4_4 = TexMobject("u^n S")

        node_0_0.move_to([-5.5, 0, 0]).scale(0.7)
        node_1_0.move_to([-3.5, -0.5, 0]).scale(0.7)
        node_1_1.move_to([-3.5, 0.5, 0]).scale(0.7)
        node_2_0.move_to([-1.5, -1, 0]).scale(0.7)
        node_2_1.move_to([-1.5, 0, 0]).scale(0.7)
        node_2_2.move_to([-1.5, 1, 0]).scale(0.7)
        # node_3_0.move_to([1, -1.5, 0])
        # node_3_1.move_to([1, -0.5, 0])
        # node_3_2.move_to([1, 0.5, 0])
        # node_3_3.move_to([1, 1.5, 0])
        node_4_0.move_to([1.0, -2, 0]).scale(0.7)
        node_4_1.move_to([1.0, -1, 0]).scale(0.7)
        node_4_2.move_to([1.0, 0, 0]).scale(0.7)
        node_4_3.move_to([1.0, 1, 0]).scale(0.7)
        node_4_4.move_to([1.0, 2, 0]).scale(0.7)

        nodes = VGroup(node_0_0,
            node_1_0,
            node_1_1,
            node_2_0,
            node_2_1,
            node_2_2,
            # node_3_0,
            # node_3_1,
            # node_3_2,
            # node_3_3,
            node_4_0,
            node_4_1,
            node_4_2,
            node_4_3,
            node_4_4
        )

        self.play(Write(nodes))
        

        call_0 = TexMobject("\\max (d^n S - K, 0)")
        call_1 = TexMobject("\\vdots")
        call_2 = TexMobject("\\max (u^j d^{n-j} S - K, 0 )")
        call_3 = TexMobject("\\vdots")
        call_4 = TexMobject("\\max (u^n S - K, 0)")

        call_0.move_to([4, -2, 0]).set_color(YELLOW).scale(0.7)
        call_1.move_to([4, -1, 0]).scale(0.7)
        call_2.move_to([4, 0, 0]).set_color(YELLOW).scale(0.7)
        call_3.move_to([4, 1, 0]).scale(0.7)
        call_4.move_to([4, 2, 0]).set_color(YELLOW).scale(0.7)

        
        self.play(Write(call_0))
        self.play(Write(call_1))
        self.play(Write(call_2))
        self.play(Write(call_3))
        self.play(Write(call_4))

        text = TexMobject("j")

        for i in range(3):
            self.add(text)
            for j in range(-2,3):
                self.play(Transform(text, text.move_to([5, j, 0])))















