from manim import *

##manim -qm a20200504_1 

class a20200504_1(Scene):
    CONFIG = {
        "n_of_steps" : 20,
        "width" : 7,
        "height" : 5,
        "radius" : 0.1,
        "origin" : np.array([-4, 0, 0])
    }

    def construct(self):

        o_text = TextMobject("$n = 0$")
        self.play(Write(o_text.move_to(LEFT*4+UP*2.5)))
        a = Circle(radius = self.radius).move_to(self.origin)
        self.play(ShowCreation(a))
        self.wait()
        self.play(Uncreate(a))

        for i in [1, 2, 5, 10, 20]:
            text = TextMobject("$n = $ {}".format(i))
            text.move_to(LEFT*4+UP*2.5)
            self.play(Transform(o_text, text))
            self.my_tree(i)
            self.wait(0.5)

        self.play(FadeOut(o_text))
        self.wait()

        
    def my_tree(self, steps):
        nodes = [
            [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
        ]
        
        for i in range(steps+1):
            for j in range(i+1): 
                location = self.origin \
                    + np.array([self.width/steps * i, 0, 0])  \
                    + np.array([0, self.height/steps * (j-i/2), 0])
                nodes[i][j].move_to(location)
            
        nodes_g = VGroup(*[nodes[i][j] for i in range(steps+1) for j in range(i+1)]) 

        self.play(ShowCreation(nodes_g), run_time = 2)
        self.wait()
        self.play(Uncreate(nodes_g))