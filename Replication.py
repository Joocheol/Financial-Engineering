from manimlib.imports import *

class Replication(Scene):
    def construct(self):

        text_010 = TextMobject("1. Replication")

        self.play(GrowFromCenter(text_010))
        self.wait(2)

        self.play(FadeOut(text_010))
        self.wait(1)

############
        game1 = TexMobject("10")
        game1_up = TexMobject("11")
        game1_down = TexMobject("11")

        game1.move_to(LEFT+DOWN)
        game1_up.move_to(RIGHT)
        game1_down.move_to(RIGHT+DOWN*2)

        arrow1 = Arrow(game1.get_right(), game1_up.get_left(), buff=0.5)
        arrow2 = Arrow(game1.get_right(), game1_down.get_left(), buff=0.5)

        text_020 = TextMobject("This is the first game.")
        text_020.to_edge(DOWN)

        self.play(Write(text_020))
        self.play(Write(game1))
        self.play(GrowArrow(arrow1))
        self.play(Write(game1_up))
        self.play(Write(game1))

        self.play(GrowArrow(arrow2))
        self.play(Write(game1_down))
        self.play(FadeOut(arrow1), FadeOut(arrow2))

        self.play(Transform(game1.copy(), game1.scale(0.7).move_to([-6,2,0])))
        self.play(Transform(game1_up.copy(), game1_up.scale(0.7).move_to([-4,3,0])))
        self.play(Transform(game1_down.copy(), game1_down.scale(0.7).move_to([-4,1,0])))
        

        self.play(FadeOut(text_020))


        game2 = TexMobject("9")
        game2_up = TexMobject("22")
        game2_down = TexMobject("0")

        game2.move_to(LEFT+DOWN)
        game2_up.move_to(RIGHT)
        game2_down.move_to(RIGHT+DOWN*2)

        text_030 = TextMobject("This is the second game.")
        text_030.to_edge(DOWN)

        self.play(Write(text_030))
        self.play(Write(game2))
        self.play(GrowArrow(arrow1))
        self.play(Write(game2_up))
        self.play(Write(game2))
        self.play(GrowArrow(arrow2))
        self.play(Write(game2_down))
        self.play(FadeOut(arrow1), FadeOut(arrow2))

        self.play(Transform(game2.copy(), game2.scale(0.7).move_to([-1,2,0])))
        self.play(Transform(game2_up.copy(), game2_up.scale(0.7).move_to([1,3,0])))
        self.play(Transform(game2_down.copy(), game2_down.scale(0.7).move_to([1,1,0])))
        
        self.play(FadeOut(text_030))

        game3 = TexMobject("?")
        game3_up = TexMobject("22")
        game3_down = TexMobject("11")

        game3.move_to(LEFT+DOWN)
        game3_up.move_to(RIGHT)
        game3_down.move_to(RIGHT+DOWN*2)

        text_040 = TextMobject("This is the third game, which we are interested in.")
        text_040.to_edge(DOWN)

        self.play(Write(text_040))
        self.play(Write(game3))
        self.play(GrowArrow(arrow1))
        self.play(Write(game3_up))
        self.play(Write(game3))
        self.play(GrowArrow(arrow2))
        self.play(Write(game3_down))
        self.play(FadeOut(arrow1), FadeOut(arrow2))

        self.play(Transform(game3.copy(), game3.scale(0.7).move_to([4,2,0])))
        self.play(Transform(game3_up.copy(), game3_up.scale(0.7).move_to([6,3,0])))
        self.play(Transform(game3_down.copy(), game3_down.scale(0.7).move_to([6,1,0])))
        self.play(FadeOut(text_040))

##########

        text_First_we_focus_on_these_numbers = TextMobject(
            "First we focus on these numbers."
        )
        text_First_we_focus_on_these_numbers.to_edge(DOWN)

        text_These_two_numbers_repesent_the_payoff_of_the_first_game = TextMobject(
            "These two numbers repesent the payoff of the first game."
        )
        text_These_two_numbers_repesent_the_payoff_of_the_first_game.to_edge(DOWN)
        rect1 = Rectangle(height=2.5, width=1.0)
        rect1.move_to([-4, 2, 0])
        rect1.set_color(RED)
        
        rect2 = Rectangle(height=2.5, width=1.0)
        rect2.move_to([1, 2, 0])
        rect2.set_color(BLUE)
        
        rect3 = Rectangle(height=2.5, width=1.0)
        rect3.set_color(YELLOW)

        
        self.play(ShowCreation(rect1))
        self.play(Write(text_First_we_focus_on_these_numbers))
        self.wait(2)
        self.play(FadeOut(text_First_we_focus_on_these_numbers))
        self.play(Write(text_These_two_numbers_repesent_the_payoff_of_the_first_game))
        self.wait(2)
        self.play(FadeOut(text_These_two_numbers_repesent_the_payoff_of_the_first_game))

        text_Now_these_two_numbers_are_the_payoff_of_the_second_game = TextMobject(
            "Now these two numbers are the payoff of the second game."
        )
        text_Now_these_two_numbers_are_the_payoff_of_the_second_game.to_edge(DOWN)
        text_With_these_two_payoffs_we_can_make_any_payoff = TextMobject(
            "With these two payoffs, we can make any payoff."
        )
        text_With_these_two_payoffs_we_can_make_any_payoff.to_edge(DOWN)
        
        self.play(ShowCreation(rect2))
        self.play(Write(text_Now_these_two_numbers_are_the_payoff_of_the_second_game))
        self.wait(2)
        self.play(FadeOut(text_Now_these_two_numbers_are_the_payoff_of_the_second_game))
        self.play(Write(text_With_these_two_payoffs_we_can_make_any_payoff))
        self.wait(3)
        self.play(FadeOut(text_With_these_two_payoffs_we_can_make_any_payoff), FadeOut(rect1), FadeOut(rect2))

        text_For_example = TextMobject(
            "For example,"
        )
        text_For_example.to_edge(DOWN)
        
        self.play(Write(text_For_example))
        self.play(FadeOut(text_For_example))

        text_by_taking = TextMobject(
            "by taking one long (+1) position in the first game (red)"
        )
        text_by_taking.to_edge(DOWN)
        
        self.play(ShowCreation(rect1))
        self.play(Write(text_by_taking))
        self.wait(2)
        self.play(FadeOut(text_by_taking))

        formula_010 = TexMobject(r"""
            \begin{bmatrix} 11 \\ 11 \end{bmatrix}
            \times (+1)
            =
            \begin{bmatrix} 11 \\ 11 \end{bmatrix}        
        """)
        formula_010.move_to(DOWN)

        self.play(Write(formula_010))

        text_and_one = TextMobject(
            "and one long (+1) position in the second game (blue)"
        )
        text_and_one.to_edge(DOWN)

        formula_020 = TexMobject(r"""
            \begin{bmatrix} 11 \\ 11 \end{bmatrix}
            \times (+1) +
            \begin{bmatrix} 22 \\ 0 \end{bmatrix}
            \times (+1)
            =
            \begin{bmatrix} 33 \\ 11 \end{bmatrix}        
        """)
        formula_020.move_to(DOWN)
        

        self.play(Write(text_and_one))
        self.play(ShowCreation(rect2))
        self.play(Transform(formula_010, formula_020))
        self.wait(3)
        self.play(FadeOut(text_and_one))



        # self.play(ShowCreation(rect3.move_to([6, 2, 0])))
        # self.wait(2)

##########

        text_Now_how = TextMobject(
            "Then how much does it cost to build this portfolio?"
        )
        text_Now_how.to_edge(DOWN)

        self.play(Write(text_Now_how))
        self.wait(3)
        self.play(FadeOut(rect1), FadeOut(rect2))
        self.play(FadeOut(text_Now_how))

        rect4 = Rectangle(height=1, width=1)
        rect4.move_to([-6, 2, 0])
        rect4.set_color(RED)

        rect5 = Rectangle(height=1, width=1)
        rect5.move_to([-1, 2, 0])
        rect5.set_color(BLUE)

        
        text_Take = TextMobject(
            "Take the current prices of the games."
        )   
        text_Take.to_edge(DOWN)

        text_And_then = TextMobject(
            "And then apply your position to the current prices")
        text_And_then.to_edge(DOWN)

        self.play(Write(text_Take))
        self.wait(1)
        self.play(ShowCreation(rect4), ShowCreation(rect5))
        self.play(FadeOut(text_Take))
        self.play(Write(text_And_then))
        self.wait(1)

        formula_030 = TexMobject(r"""
        \begin{bmatrix} 10\end{bmatrix}
        \times (+1) +
        \begin{bmatrix} 9\end{bmatrix}
        \times (+1)
        =
        \begin{bmatrix} 19\end{bmatrix}        
        """)
        formula_030.move_to(DOWN)

        self.play(FadeOut(formula_020))
        self.wait(5)
        self.play(Transform(formula_010, formula_030))

 
        
        
        #self.add(formula.shift(DOWN))
        #self.wait(1)

        formula_020 = TexMobject(r"""
        \begin{bmatrix}  ?? \\ ?? \end{bmatrix}
        \times x_1 +
        \begin{bmatrix} 22 \\ 0 \end{bmatrix}
        \times x_2
        =
        \begin{bmatrix} 22 \\ 11 \end{bmatrix}        
        """)
       
        #self.play(ReplacementTransform(formula, formula_020))
        #self.wait(1)


