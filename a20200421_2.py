from manimlib.imports import *

r = 1
up_node = 15
down_node = 10

class a20200421_2(Scene):
    def construct(self):
        
        layer1 = []
        for i in range(up_node):
            layer1.append(Circle(radius=r))
            layer1[i].move_to([8*(i-up_node)/up_node+4, 3, 0]).scale(0.2).set_color(WHITE)
            self.play(ShowCreation(layer1[i]), run_time=0.1)
           

        layer2 = []
        for i in range(down_node):
            layer2.append(Circle(radius=r))
            layer2[i].move_to([6*(i-down_node)/down_node+3, -3, 0]).scale(0.2).set_color(WHITE)
            self.play(ShowCreation(layer2[i]), run_time=0.1)

        lines = []
        for i in range(up_node):
            for j in range(down_node):
                s = layer1[i].get_center()
                e = layer2[j].get_center()
                lines.append(Line(s, e))

        lines_g = VGroup(*lines)
        self.play(ShowCreation(lines_g))