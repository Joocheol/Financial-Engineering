from manimlib.imports import *

class full_tree(Scene):
    def construct(self):

        node_0_0 = Tex("S")
        node_1_0 = Tex("d S")
        node_1_1 = Tex("u S")
        node_2_0 = Tex("d^2 S")
        node_2_1 = Tex("ud S")
        node_2_2 = Tex("u^2 S")
        # node_3_0 = Tex("\\ddots")
        # node_3_1 = Tex("")
        # node_3_2 = Tex("")
        # node_3_3 = Tex("\\iddots")
        node_4_0 = Tex("d^n S")
        node_4_1 = Tex("\\vdots")
        node_4_2 = Tex("u^j d^{n-j} S")
        node_4_3 = Tex("\\vdots")
        node_4_4 = Tex("u^n S")

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
        

        call_0 = Tex("\\max (d^n S - K, 0)")
        call_1 = Tex("\\vdots")
        call_2 = Tex("\\max (u^j d^{n-j} S - K, 0 )")
        call_3 = Tex("\\vdots")
        call_4 = Tex("\\max (u^n S - K, 0)")

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

        text = Tex("j")

        for i in range(3):
            self.add(text)
            for j in range(-2,3):
                self.play(Transform(text, text.move_to([5, j, 0])))

class nodes_to_line(Scene):
    def construct(self):

        nodes = Tex(
            "u^{0} d^{n-0} S",
            "u^{1} d^{n-1} S",
            "\\vdots",
            "u^j d^{n-j} S",
            "\\vdots",
            "u^{n-1} d^1 S", 
            "u^{n} d^{n-n} S", 
             )

        [nodes[i].move_to([-5, i-3, 0]) for i in range(7)]

        line = Line([-3,-0.5,0], [5,-0.5,0])

        self.play(Write(nodes))
        self.play(ShowCreation(line))
        #self.play(Transform(nodes, nodes.move_to([-2, -1, 0])))
        self.play(Rotate(nodes, angle=PI/2, axis=IN, about_point=[-3,-4,0]))

        line_1 = Line([-3,-0.5,0], [1,-0.5,0])
        line_2 = Line([1,-0.5,0], [5,3,0])

        line_1.set_color(RED)
        line_2.set_color(RED)

        self.play(ShowCreation(line_1))
        self.play(ShowCreation(line_2))

        self.play(Rotate(nodes, angle=PI/2, axis=OUT, about_point=[-3,-4,0]))














