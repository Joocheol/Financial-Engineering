from manimlib.imports import *

class a20200522_4(Scene):
    def construct(self):

        title_1 = TextMobject("The simplest case")
        title_1.to_edge(UP, buff=1)
        self.play(Write(title_1))
        self.wait()

        x_equal = TexMobject("x = ")
        x_mat = Matrix([5,6,"\\vdots",8], element_alignment_corner=DOWN)
        obj_1 = VGroup(x_equal,x_mat).arrange_submobjects()

        y_equal = TexMobject("y = ") 
        obj_1 = VGroup(obj_1,y_equal).arrange_submobjects(buff=1)

        y_mat = Matrix([21,31,"\\vdots",63], element_alignment_corner=DOWN)
        obj_1 = VGroup(obj_1,y_mat).arrange_submobjects()

        
        self.play(ShowCreation(obj_1))
        self.wait()

###

        title_2 = TextMobject("More Features")
        title_2.to_edge(UP, buff=1)
        self.play(ReplacementTransform(title_1, title_2))
        self.wait()

        x_equal = TexMobject("x = ")
        x_mat = Matrix( [ [5,2],  [4,6], "\\vdots", [8,8] ], element_alignment_corner=DOWN )
        obj_2 = VGroup(x_equal,x_mat).arrange_submobjects()

        y_equal = TexMobject("y = ") 
        obj_2 = VGroup(obj_2,y_equal).arrange_submobjects(buff=1)

        y_mat = Matrix([21,31,"\\vdots",63], element_alignment_corner=DOWN)
        obj_2 = VGroup(obj_2,y_mat).arrange_submobjects()

        
        self.play(ReplacementTransform(obj_1, obj_2))
        self.wait()

#

        title_3 = TextMobject("Or classification")
        title_3.to_edge(UP, buff=1)
        self.play(ReplacementTransform(title_2, title_3))
        self.wait()

        x_equal = TexMobject("x = ")
        x_mat = Matrix( [ [5,2],  [4,6], "\\vdots", [8,8] ], element_alignment_corner=DOWN )
        obj_3 = VGroup(x_equal,x_mat).arrange_submobjects()

        y_equal = TexMobject("y = ") 
        obj_3 = VGroup(obj_3,y_equal).arrange_submobjects(buff=1)

        y_mat = Matrix(['cat','dog',"\\vdots",'dog'], element_alignment_corner=DOWN)
        obj_3 = VGroup(obj_3,y_mat).arrange_submobjects()

        equal_sign = TexMobject("=")
        obj_3 = VGroup(obj_3,equal_sign).arrange_submobjects()

        y_mat_2 = Matrix([[1,0],[0,1],"\\vdots",[0,1]], element_alignment_corner=DOWN)
        obj_3 = VGroup(obj_3,y_mat_2).arrange_submobjects()


        
        self.play(ReplacementTransform(obj_2, obj_3))
        self.wait()