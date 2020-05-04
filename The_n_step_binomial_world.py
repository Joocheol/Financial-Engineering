from manimlib.imports import *

class title(Scene):
    def construct(self):

        title = TextMobject("The $n$-step Binomial World")

        self.play(Write(title))
        self.wait()

class intro(Scene):
    CONFIG = {
        "n_of_steps" : 20,
        "width" : 7,
        "height" : 5,
        "radius" : 0.1,
        "origin" : np.array([-4, 0, 0])
    }
    
    def construct(self):

        nodes = [
            [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
        ]
        
        for i in range(self.n_of_steps+1):
            for j in range(i+1): 
                location = self.origin \
                    + np.array([self.width/self.n_of_steps * i, 0, 0])  \
                    + np.array([0, self.height/self.n_of_steps * (j-i/2), 0])
                nodes[i][j].move_to(location)
        
        center = TextMobject("In this world, we have").scale(0.7)
        self.play(Write(center.shift(LEFT*0.5)))

        nodes_g = VGroup(*[nodes[0][0]])
        self.play(Write(nodes_g), run_time=1)
        text_1 = TextMobject("Present").scale(0.7)
        self.play(Write(text_1.next_to(nodes[0][0], LEFT)))

    
        nodes_g = VGroup(*nodes[self.n_of_steps])
        self.play(Write(nodes_g), run_time=1)
        text_2 = TextMobject("Future").scale(0.7)
        brace = Brace(nodes_g, RIGHT)
        self.play(Write(brace))
        self.play(Write(text_2.next_to(brace, RIGHT)))
                
        center_1 = TextMobject("They are connected").scale(0.7)
        self.play(Transform(center, center_1.shift(LEFT*0.5)))
        self.wait(2)
        self.play(FadeOut(center))

        nodes_g = VGroup(*[nodes[i][j] for i in range(1, self.n_of_steps) for j in range(i+1)])
        self.play(ShowCreation(nodes_g), run_time = 2)
        self.wait()
        self.play(FadeOut(nodes_g))
        text_3 = TextMobject("This is the binomial world").scale(0.7)
        self.play(Write(text_3.shift(LEFT*0.5)))
        self.wait()
        self.play(ShowCreationThenFadeOut(nodes_g))
        self.wait()

class steps(Scene):
    CONFIG = {
        "n_of_steps" : 20,
        "width" : 7,
        "height" : 5,
        "radius" : 0.1,
        "origin" : np.array([-4, 0, 0])
    }

    def construct(self):

        for i in [1, 2, 5, 10, 20]:
            self.my_tree(i)
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

        self.play(ShowCreation(nodes_g))
        self.wait()
        self.play(Uncreate(nodes_g))
    
    # def construct(self):

    #     nodes = [
    #         [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
    #     ]
        
    #     for i in range(self.n_of_steps+1):
    #         for j in range(i+1): 
    #             location = self.origin \
    #                 + np.array([self.width/self.n_of_steps * i, 0, 0])  \
    #                 + np.array([0, self.height/self.n_of_steps * (j-i/2), 0])
    #             nodes[i][j].move_to(location)
        
    #     center = TextMobject("It starts from").scale(0.7)
    #     self.play(Write(center.shift(LEFT*0.5)))

    #     nodes_g = VGroup(*[nodes[0][0]])
    #     self.play(Write(nodes_g), run_time=1)
    #     text_1 = TextMobject("Present").scale(0.7)
    #     self.play(Write(text_1.next_to(nodes[0][0], LEFT)))

    #     nodes_g = VGroup(*nodes[self.n_of_steps])
    #     self.play(Write(nodes_g), run_time=1)
    #     text_2 = TextMobject("Future").scale(0.7)
    #     brace = Brace(nodes_g, RIGHT)
    #     self.play(Write(brace))
    #     self.play(Write(text_2.next_to(brace, RIGHT)))



    # 