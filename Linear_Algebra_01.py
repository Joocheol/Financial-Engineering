from manimlib.imports import *

class MyScene(Scene):

    def add_vector(self, vector, color=YELLOW, animate=True, **kwargs):
        if not isinstance(vector, Arrow):
            vector = Vector(vector, color=color, **kwargs)
        if animate:
            self.play(GrowArrow(vector))
        self.add(vector)
        return vector

    def write_vector_coordinates(self, vector, **kwargs):
        coords = vector_coordinate_label(vector, **kwargs)
        #self.play(Write(coords))
        self.add(coords)
        return coords

class Linear_Algebra_01(Scene):
    def construct(self):

        self.intro()

    def intro(self):
        text_1 = TextMobject("``Cogito ergo sum.''")
        #text_2 = TextMobject('English: "I think, therefore I am"')
        text_3 = TextMobject("by Ren\\'{e} Descartes")
        
        self.play(Write(text_1))
        #self.play(Write(text_2.next_to(text_1, DOWN)))
        self.play(Write(text_3.next_to(text_1, DOWN)))
        
        self.wait()
        return None

class Linear_Algebra_02(VectorScene):
    def construct(self):

        v_1 = self.add_vector([-2,3])
        self.write_vector_coordinates(v_1)
        self.wait()
        
        self.vector_to_coords(v_1)

class Linear_Algebra_03(MyScene):
    def construct(self):

        plane = NumberPlane()

        v_1 = self.add_vector([-2,-3])
        self.write_vector_coordinates(v_1)
        self.wait()
        
        #self.vector_to_coords(v_1)

    #     v_2 = self.get_vector([1,2])

    # def get_vector(self, numerical_vector, **kwargs):
    #     return Arrow(
    #         plane.coords_to_point(0, 0),
    #         plane.coords_to_point(*numerical_vector[:2]),
    #         buff=0,
    #         **kwargs
    #     )

        self.tex("hello")


    

