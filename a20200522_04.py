from manimlib.imports import *

class a20200522_04(Scene):
    def construct(self):
####
        title_1 = TextMobject("The simplest case")
        title_1.to_edge(UP, buff=1)
        self.play(Write(title_1))
        #self.wait()

        x_equal = Tex("x = ")
        x_mat = Matrix([5,8,10,"\\vdots",6.5], element_alignment_corner=DOWN)
        obj_1 = VGroup(x_equal,x_mat).arrange_submobjects()

        y_equal = Tex("y = ") 
        obj_1 = VGroup(obj_1,y_equal).arrange_submobjects(buff=1)

        y_mat = Matrix([21,31,40.8,"\\vdots",63], element_alignment_corner=DOWN)
        obj_1 = VGroup(obj_1,y_mat).arrange_submobjects()
        obj_1.scale(0.7).to_edge(LEFT, buff=1)

        self.play(ShowCreation(obj_1))
        self.wait()

####



####

        code_1 = Tex(r"\texttt{Dense(1, input\textunderscore shape=[1])} ")
        code_1.scale(0.7).to_edge(RIGHT, buff=1)

        self.play(ShowCreation(code_1))
        self.wait()

    
####

        title_2 = TextMobject("If there are more than 1 feature")
        title_2.to_edge(UP, buff=1)
        self.play(ReplacementTransform(title_1, title_2))
        #self.wait()

        x_equal = Tex("x = ")
        x_mat = Matrix( [ [5,2],  [4,6], "\\vdots", [8,8] ], element_alignment_corner=DOWN )
        obj_2 = VGroup(x_equal,x_mat).arrange_submobjects()

        y_equal = Tex("y = ") 
        obj_2 = VGroup(obj_2,y_equal).arrange_submobjects(buff=1)

        y_mat = Matrix([21,31,"\\vdots",63], element_alignment_corner=DOWN)
        obj_2 = VGroup(obj_2,y_mat).arrange_submobjects()
        obj_2.scale(0.7).to_edge(LEFT, buff=1)

        
        self.play(ReplacementTransform(obj_1, obj_2))
        self.wait()

####

        code_2 = Tex(r"\texttt{Dense(1, input\textunderscore shape=[2])} ")
        code_2.scale(0.8).to_edge(RIGHT, buff=1)

        self.play(ReplacementTransform(code_1, code_2))
        self.wait()
    
####

#

        title_3 = TextMobject("For the classification problem")
        title_3.to_edge(UP, buff=1)
        self.play(ReplacementTransform(title_2, title_3))
        self.wait()

        x_equal = Tex("x = ")
        x_mat = Matrix( [ [5,2,0],  [4,1,6], "\\vdots", [8,8,6] ], element_alignment_corner=DOWN )
        obj_3 = VGroup(x_equal,x_mat).arrange_submobjects()

        y_equal = Tex("y = ") 
        obj_3 = VGroup(obj_3,y_equal).arrange_submobjects(buff=1)

        y_mat = Matrix(['cat','dog',"\\vdots",'dog'], element_alignment_corner=DOWN)
        obj_3 = VGroup(obj_3,y_mat).arrange_submobjects()

        equal_sign = Tex("=")
        obj_3 = VGroup(obj_3,equal_sign).arrange_submobjects()

        y_mat_2 = Matrix([[1,0],[0,1],"\\vdots",[0,1]], element_alignment_corner=DOWN)
        obj_3 = VGroup(obj_3,y_mat_2).arrange_submobjects()
        obj_3.scale(0.7).to_edge(LEFT, buff=1)


        
        self.play(ReplacementTransform(obj_2, obj_3))
        self.wait()

####

        code_3 = Tex(r"\texttt{Dense(1, input\textunderscore shape=[3])} ")
        code_4 = Tex(r"\texttt{Dense(2)} ")

        code_5 = VGroup(code_3, code_4).arrange_submobjects(DOWN, aligned_edge=LEFT)
        code_5.scale(0.7).to_edge(RIGHT, buff=1)

        self.play(ReplacementTransform(code_2, code_5))
        self.wait()
    
####