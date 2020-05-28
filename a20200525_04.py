from manimlib.imports import *

class a20200525_04(GraphScene):


    CONFIG = {
        "y_max" : 7,
        "y_min" : -7,
        "x_min" : 0,
        "x_max" : 10,
        "graph_origin": [-1,0,0],
        "x_axis_label" : "$S_T$",
        "x_axis_width": 7,
        "y_axis_label" : "",
    }

    def construct(self):

        self.setup_axes()
        
#### Math formulas

        string = r"""\max ( S_T - K , 0 )"""
        string = string.split()
        call_long = TexMobject(*string)

        string = r"""-\max ( S_T - K , 0 )"""
        string = string.split()
        call_short = TexMobject(*string)

        string = r"""\max ( K - S_T , 0 )"""
        string = string.split()
        put_long = TexMobject(*string)

        string = r"""-\max ( K - S_T , 0 )"""
        string = string.split()
        put_short = TexMobject(*string)

        string = r"""S_T - K"""
        string = string.split()
        forward_long = TexMobject(*string)

        string = r"""K - S_T"""
        string = string.split()
        forward_short = TexMobject(*string)

        string = r"""S_T"""
        string = string.split()
        asset_long = TexMobject(*string)

        string = r"""-S_T"""
        string = string.split()
        asset_short = TexMobject(*string)

        string = r"""K"""
        string = string.split()
        money_long = TexMobject(*string)

        string = r"""-K"""
        string = string.split()
        money_short = TexMobject(*string)

#### Graphs

        c_long_5 = lambda x : max(x - 5, 0)
        c_long_5 = self.get_graph(c_long_5, color="YELLOW")
        
        c_short_5 = lambda x : -max(x - 5, 0)
        c_short_5 = self.get_graph(c_short_5, color="YELLOW")

        p_long_5 = lambda x : max(5 - x, 0)
        p_long_5 = self.get_graph(p_long_5, color="YELLOW")
        
        p_short_5 = lambda x : -max(5 - x, 0)
        p_short_5 = self.get_graph(p_short_5, color="YELLOW")

        f_long_5 = lambda x : x-5
        f_long_5 = self.get_graph(f_long_5, color="YELLOW")
        
        f_short_5 = lambda x : 5-x
        f_short_5 = self.get_graph(f_short_5, color="YELLOW")

        s_long = lambda x : x
        s_long = self.get_graph(s_long, color="YELLOW")
        
        s_short = lambda x : -x
        s_short = self.get_graph(s_short, color="YELLOW")

        m_long_5 = lambda x : 5
        m_long_5 = self.get_graph(m_long_5, color="YELLOW")
        
        m_short_5 = lambda x : -5
        m_short_5 = self.get_graph(m_short_5, color="YELLOW")
       
#####
         
        text = TextMobject("It was fast.").to_edge(UL, buff=1)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        text = TextMobject("Let's review one by one.").to_edge(UL, buff=1)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        self.play(ShowCreation(s_long))
        self.play(Write(asset_long.to_edge(LEFT, buff=1)))
        self.wait(2)

        text = TextMobject("What is this?").to_edge(UL, buff=1)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        text = TextMobject("This is the payoff you will get at time $T$,").to_edge(UL, buff=1)
        text_2 = TextMobject("if you buy the underlying asset at time $0$.").next_to(text, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(text))
        self.play(Write(text_2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text_2))

        text = TextMobject("But you didn't have money to buy the asset,").to_edge(UL, buff=1)
        text_2 = TextMobject("which was $S_0$ at time $0$.").next_to(text, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(text))
        self.play(Write(text_2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text_2))

        text = TextMobject("So, you decided to borrow $S_0$ to buy the asset, ").to_edge(UL, buff=1)
        text_2 = TextMobject("and promised to pay back $S_0 r$ at time $T$.").next_to(text, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(text))
        self.play(Write(text_2))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(text_2))

        text = TextMobject("Now you need to add $K = S_0 r$ in the graph, ").to_edge(UL, buff=1)
        text_2 = TextMobject("with the minus sign $(-)$.").next_to(text, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(Write(text))
        self.play(Write(text_2))
        
        self.play(ShowCreation(m_short_5))
        self.play(Transform(asset_long, forward_long.to_edge(LEFT, buff=1)))
        self.wait(2)

        self.play(Transform(s_long, f_long_5), Transform(m_short_5, f_long_5))
        self.wait(5)

        






        # self.play(ShowCreation(c_short_5))
        # self.play(Write(call_short.to_edge(LEFT, buff=1)))
        # self.wait()
        # self.play(FadeOut(call_short))
        # self.play(FadeOut(c_short_5))

        # self.play(ShowCreation(f_long_5))
        # self.play(Write(forward_long.to_edge(LEFT, buff=1)))
        # self.wait()
        # self.play(FadeOut(forward_long))
        # self.play(FadeOut(f_long_5))

        

        # self.play(ShowCreation(p_long_5))
        # self.play(Write(put_long.to_edge(LEFT, buff=1)))
        # self.wait()
        # self.play(FadeOut(put_long))
        # self.play(FadeOut(p_long_5))

        # self.play(ShowCreation(p_short_5))
        # self.play(Write(put_short.to_edge(LEFT, buff=1)))
        # self.wait()
        # self.play(FadeOut(put_short))
        # self.play(FadeOut(p_short_5))

        # self.play(ShowCreation(m_short_5))
        # self.play(Write(money_short.to_edge(LEFT, buff=1)))
        # self.wait()
        # self.play(FadeOut(money_short))
        # self.play(FadeOut(m_short_5))

        # text = TextMobject("It is a showtime!").to_edge(UL, buff=1)
        # self.play(Write(text))
        # self.wait()
        # self.play(FadeOut(text))

        # group = VGroup(call_long, put_short).arrange_submobjects(DOWN).to_edge(LEFT, buff=1)
        # self.play(Write(group))
        # self.wait()
        # self.play(ShowCreation(c_long_5))
        # self.play(ShowCreation(p_short_5))
        # self.wait()
        # self.play(Transform(group, forward_long))
        # self.wait()
        # self.play(FadeOut(c_long_5), FadeOut(p_short_5), FadeOut(group))

        # self.play(ShowCreation(f_long_5))
        # self.play(Write(forward_long))
        # self.play(Transform(f_long_5.copy(), s_long), Transform(f_long_5.copy(), m_short_5))
        # self.wait()
        # self.play(FadeOut(f_long_5))
        # self.wait()






