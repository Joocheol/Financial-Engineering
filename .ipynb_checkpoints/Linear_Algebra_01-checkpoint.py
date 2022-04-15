from manimlib.imports import *

class LA_01(Scene):
    def construct(self):

        text_010 = TextMobject("Can you solve the system of equations")

        # self.play(GrowFromCenter(text_010))
        # self.wait(1)

        # self.play(FadeOut(text_010))
        # self.wait(1)

        formula_010 = Tex(r"""
            x + y = 1  \\
            x - y = 1 
        """)

        self.play(GrowFromCenter(formula_010))
        self.wait(1)

        text_030 = TextMobject("We know how to solve the system of equations.")
        text_030.to_edge(DOWN)

        self.play(Write(text_030))
        self.wait()
        self.play(FadeOut(text_030))

        text_040 = TextMobject("One way is to use the graph.")
        text_040.to_edge(DOWN)

        self.play(Write(text_040))

        formula_010.scale(0.7)
        self.play(formula_010.to_edge, UL )

        plane = NumberPlane()
        self.add(plane)
        self.wait()
        self.play(FadeOut(text_040))

        f1 = FunctionGraph(
            lambda x: 1 - x,
        )
        self.play(ShowCreation(f1))

        f2 = FunctionGraph(
            lambda x: x - 1,
        )
        self.play(ShowCreation(f2))

class LA_test(Scene):

    print(color_to_rgba(Color('blue')))
    print(rgb_to_color(np.array([0,1,0])))
    print(random_bright_color())
    

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
        return self

class Linear_Algebra_02(VectorScene):
    def construct(self):

        v_1 = self.add_vector([-2,3])
        self.write_vector_coordinates(v_1)
        self.wait()
        
        self.vector_to_coords(v_1)

        self.get_basis_vector_labels(at_tip=True)

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

class LA_04(Scene):
    CONFIG = {
        "quote": ["Cogito ergo sum."],
        "quote_arg_separator": " ",
        "highlighted_quote_terms": {},
        "author": "Ren\\'{e} Descartes",
        "fade_in_kwargs": {
            "lag_ratio": 0.5,
            "rate_func": linear,
            "run_time": 5,
        },
        "text_size": "\\Large",
        "use_quotation_marks": True,
        "top_buff": 1.0,
        "author_buff": 1.0,
    }

    def construct(self):
        self.quote = self.get_quote()
        self.author = self.get_author(self.quote)

        self.play(FadeIn(self.quote, **self.fade_in_kwargs))
        self.wait(2)
        self.play(Write(self.author, run_time=3))
        self.wait()

    def get_quote(self, max_width=FRAME_WIDTH - 1):
        text_mobject_kwargs = {
            "alignment": "",
            "arg_separator": self.quote_arg_separator,
        }
        if isinstance(self.quote, str):
            if self.use_quotation_marks:
                quote = TextMobject("``%s''" %
                                    self.quote.strip(), **text_mobject_kwargs)
            else:
                quote = TextMobject("%s" %
                                    self.quote.strip(), **text_mobject_kwargs)
        else:
            if self.use_quotation_marks:
                words = [self.text_size + " ``"] + list(self.quote) + ["''"]
            else:
                words = [self.text_size] + list(self.quote)
            quote = TextMobject(*words, **text_mobject_kwargs)
            # TODO, make less hacky
            if self.quote_arg_separator == " ":
                quote[0].shift(0.2 * RIGHT)
                quote[-1].shift(0.2 * LEFT)
        for term, color in self.highlighted_quote_terms:
            quote.set_color_by_tex(term, color)
        quote.to_edge(UP, buff=self.top_buff)
        if quote.get_width() > max_width:
            quote.set_width(max_width)
        return quote

    def get_author(self, quote):
        author = TextMobject(self.text_size + " --" + self.author)
        author.next_to(quote, DOWN, buff=self.author_buff)
        author.set_color(YELLOW)
        return author


    

