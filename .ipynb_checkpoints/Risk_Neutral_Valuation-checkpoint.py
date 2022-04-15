from manimlib.imports import *

class Risk_Neutral_Valuation(Scene):
    def construct(self):

        title = TextMobject("3. Risk Neutral Valuation")

        self.play(GrowFromCenter(title))
        self.wait(2)
        self.play(FadeOut(title))

        text = TextMobject("Let's start with numbers.")
        text.to_edge(DOWN)

        self.play(Write(text))
        self.wait(1)

        formula = Tex(
            "22 \\times ", 
            "\\frac{\\frac{9}{22}}{\\frac{9}{22}+\\frac{11}{22}} ",
            "\\times ",
            "(\\frac{_9}{^{22}}+\\frac{_{11}}{^{22}})",
            " + 11 \\times ",
            "\\frac{\\frac{11}{22}}{\\frac{9}{22}+\\frac{11}{22}} ",
            "\\times ",
            "(\\frac{_9}{^{22}}+\\frac{_{11}}{^{22}}) "
        )

        self.play(Write(formula))
        self.wait(1)

        self.play(formula.move_to, 2*UP)
        self.wait(1)

        self.play(FadeOut(text))

        text = TextMobject("We have seen all these numbers, complicated though.")
        text.to_edge(DOWN)

        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))

        text = TextMobject("Notice that these parts can be cancelled out.")
        text.to_edge(DOWN)

        brace1 = Brace(formula[1], DOWN, buff = SMALL_BUFF)
        brace2 = Brace(formula[3], DOWN, buff = SMALL_BUFF)
        brace3 = Brace(formula[5], DOWN, buff = SMALL_BUFF)
        brace4 = Brace(formula[7], DOWN, buff = SMALL_BUFF)

        self.play(
            Write(text),
            GrowFromCenter(brace1),
            GrowFromCenter(brace2),
            GrowFromCenter(brace3),
            GrowFromCenter(brace4)
        )
        self.wait(2)

        self.play(FadeOut(text))

        text = TextMobject("There is a reason to keep them here.")
        text.to_edge(DOWN)

        self.play(
            Write(text),
            FadeOut(brace1),
            FadeOut(brace2),
            FadeOut(brace3),
            FadeOut(brace4)
        )
        self.wait(1)

        self.play(FadeOut(text))
        text = TextMobject("The answer to this equation is 14.5 as usual.")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))
        text = TextMobject("Each element in the equation has a special meaning.")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))
        text = TextMobject("What are these?")
        text.to_edge(DOWN)

        framebox1 = SurroundingRectangle(formula[1], buff = .1)
        framebox2 = SurroundingRectangle(formula[5], buff = .1)

        self.play(
            Write(text),
            ShowCreation(framebox1),
            ShowCreation(framebox2),
        )
        self.wait(2)

        self.play(FadeOut(text), FadeOut(framebox1), FadeOut(framebox2),)
        text = TextMobject("What are these?")
        text.to_edge(DOWN)

        framebox1 = SurroundingRectangle(formula[3], buff = .1)
        framebox2 = SurroundingRectangle(formula[7], buff = .1)

        self.play(Write(text), ShowCreation(framebox1), ShowCreation(framebox2))
        self.wait(2)

        self.play(FadeOut(text), FadeOut(framebox1), FadeOut(framebox2),)
        text = TextMobject("What are these?")
        text.to_edge(DOWN)

        framebox1 = SurroundingRectangle(formula[0], buff = .1)
        framebox2 = SurroundingRectangle(formula[4], buff = .1)

        self.play(Write(text), ShowCreation(framebox1), ShowCreation(framebox2))
        self.wait(2)

        self.play(FadeOut(text), FadeOut(framebox1), FadeOut(framebox2),)
        text = TextMobject("With all these, we have the risk neutral valuation formula.")
        text.to_edge(DOWN)

        formula = TextMobject(
            "\\textrm{df} ", 
            "E",
            "(X)"
        )

        self.play(Write(formula))
        self.wait(1)
        self.play(Write(text))
        self.wait(2)


