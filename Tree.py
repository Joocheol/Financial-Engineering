from manimlib.imports import *

class Tree(Scene):
    CONFIG = {
        "n_of_steps" : 10,
        "height" : 6,
        "width" : 5,
        "radius" : 0.1,
        "origin" : np.array([0, 3, 0])
    }
    
    def construct(self):

        nodes = [
            [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
        ]
        
        for i in range(self.n_of_steps+1):
            for j in range(i+1): 
                location = self.origin \
                    + np.array([0, self.height/self.n_of_steps * -i, 0])  \
                    + np.array([self.width/self.n_of_steps * (j-i/2), 0, 0])
                self.play(Write(nodes[i][j].move_to(location)), run_time = 0.1)

class Tree1(Scene):
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
            nodes_g = VGroup(*nodes[i]) 

            if i == 0:
                self.play(Write(nodes_g), run_time=1)
                text_1 = TextMobject("Present")
                self.play(Write(text_1.next_to(nodes[0][0], LEFT)))

            if i == self.n_of_steps:
                self.play(Write(nodes_g), run_time=1)
                text_2 = TextMobject("Maturity")
                nodes_g = VGroup(*nodes[self.n_of_steps])
                brace = Brace(nodes_g, RIGHT)
                self.play(Write(brace))
                self.play(Write(text_2.next_to(brace, RIGHT)))
                
        for i in range(1,self.n_of_steps):
            nodes_g = VGroup(*nodes[i]) 
            self.play(Write(nodes_g), run_time=0.2)

        text_1 = TextMobject("Present")
        text_2 = TextMobject("Maturity")


class Tree2(Scene):
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
            nodes_g = VGroup(*nodes[i]) 

            self.add(nodes_g)

        first_rand = np.random.randint(self.n_of_steps)
        second_rand = np.random.randint(first_rand)

        self.play(FocusOn(nodes[first_rand][second_rand]))
        for _ in range(5):
            self.play(Indicate(nodes[first_rand][second_rand]))
        for _ in range(5):
            self.play(
                Indicate(nodes[first_rand+1][second_rand]), 
                Indicate(nodes[first_rand+1][second_rand+1])
            )

        was = 0
        for i in range(self.n_of_steps+1):
            self.play(Indicate(nodes[i][was]), run_time = 0.5)
            self.add(nodes[i][was].set_color(YELLOW))
            was = was + np.random.randint(2)

        self.wait()


                #self.play(Write(nodes[i][j].move_to(location)), run_time = 0.01)


        #nodes_g = VGroup(nodes[0][0], nodes[1][0], nodes[1][1])
        ##nodes_g = VGroup(*nodes[self.n_of_steps-3])
        # self.play(
        #     AnimationOnSurroundingRectangle(nodes[0][0]),
        #     AnimationOnSurroundingRectangle(nodes[1][0]),
        #     AnimationOnSurroundingRectangle(nodes[1][1]), 
        # )
        ##self.play(AnimationOnSurroundingRectangle(nodes_g))

class Tree3(Scene):
    CONFIG = {
        "n_of_steps" : 20,
        "width" : 7,
        "height" : 5,
        "radius" : 0.1,
        "origin" : np.array([-4, 0, 0])
    }
    
    def construct(self):

        for i in range(1, 10):
            self.my_tree(i)

        
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
        self.play(Uncreate(nodes_g))
