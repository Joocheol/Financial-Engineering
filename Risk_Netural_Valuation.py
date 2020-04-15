#!/usr/bin/env python



from manimlib.imports import *



class Risk_Neutral_Valuation(Scene):

    def construct(self):



        text_010 = TextMobject("3. Risk Neutral Valuation")



        self.play(

            Write(text_010)

        )

        self.wait(2)

        

        self.play(

            FadeOut(text_010)

        )



 

        formula_010 = TexMobject(

            "22 \\times ", 

            "\\frac{\\frac{9}{22}}{\\frac{9}{22}+\\frac{11}{22}} ",

            "\\times ",

            "(\\frac{_9}{^{22}}+\\frac{_{11}}{^{22}})",

            " + 11 \\times ",

            "\\frac{\\frac{11}{22}}{\\frac{9}{22}+\\frac{11}{22}} ",

            "\\times ",

            "(\\frac{_9}{^{22}}+\\frac{_{11}}{^{22}}) "

        )



        self.play(

            Write(formula_010)

        )

        self.wait(1)



        self.play(

            formula_010.move_to, 2*UP

        )

        self.wait(1)

# brace

        brace1 = Brace(formula_010[1], DOWN, buff = SMALL_BUFF)

        brace2 = Brace(formula_010[3], DOWN, buff = SMALL_BUFF)



        self.play(

            GrowFromCenter(brace1),

            GrowFromCenter(brace2)

        )

# New

        text=TexMobject(

            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",

            "g(x)\\frac{d}{dx}f(x)"

        )

        self.play(Write(text))

        framebox1 = SurroundingRectangle(text[1], buff = .1)

        framebox2 = SurroundingRectangle(text[3], buff = .1)

        t1 = TexMobject("g'f")

        t2 = TexMobject("f'g")

        t1.next_to(framebox1, UP, buff=0.1)

        t2.next_to(framebox2, UP, buff=0.1)

        self.play(

            ShowCreation(framebox1),

            FadeIn(t1)

            )

        self.wait()

        self.play(

            ReplacementTransform(framebox1.copy(),framebox2),

            ReplacementTransform(t1.copy(),t2),

            )

        self.wait()























# To watch one of these scenes, run the following:

# python -m manim example_scenes.py SquareToCircle -pl

#

# Use the flat -l for a faster rendering at a lower

# quality.

# Use -s to skip to the end and just save the final frame

# Use the -p to have the animation (or image, if -s was

# used) pop up once done.

# Use -n <number> to skip ahead to the n'th animation of a scene.

# Use -r <number> to specify a resolution (for example, -r 1080

# for a 1920x1080 video)





# class OpeningManimExample(Scene):

#     def construct(self):

#         title = TextMobject("This is some \\LaTeX")

#         basel = TexMobject(

#             "\\sum_{n=1}^\\infty "

#             "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"

#         )

#         VGroup(title, basel).arrange(DOWN)

#         self.play(

#             Write(title),

#             FadeInFrom(basel, UP),

#         )

#         self.wait()



#         transform_title = TextMobject("That was a transform")

#         transform_title.to_corner(UP + LEFT)

#         self.play(

#             Transform(title, transform_title),

#             LaggedStart(*map(FadeOutAndShiftDown, basel)),

#         )

#         self.wait()



#         grid = NumberPlane()

#         grid_title = TextMobject("This is a grid")

#         grid_title.scale(1.5)

#         grid_title.move_to(transform_title)



#         self.add(grid, grid_title)  # Make sure title is on top of grid

#         self.play(

#             FadeOut(title),

#             FadeInFromDown(grid_title),

#             ShowCreation(grid, run_time=3, lag_ratio=0.1),

#         )

#         self.wait()



#         grid_transform_title = TextMobject(

#             "That was a non-linear function \\\\"

#             "applied to the grid"

#         )

#         grid_transform_title.move_to(grid_title, UL)

#         grid.prepare_for_nonlinear_transform()

#         self.play(

#             grid.apply_function,

#             lambda p: p + np.array([

#                 np.sin(p[1]),

#                 np.sin(p[0]),

#                 0,

#             ]),

#             run_time=3,

#         )

#         self.wait()

#         self.play(

#             Transform(grid_title, grid_transform_title)

#         )

#         self.wait()

