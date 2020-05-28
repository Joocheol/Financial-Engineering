from manimlib.imports import *

class a20200524_14(GraphScene):


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
        # c = lambda x : max(x - 3, 0)
        # c = self.get_graph(c)
        # self.add(c)

        # p = lambda x : -max(3 - x, 0)
        # p = self.get_graph(p)
        # self.add(p)

        # s = lambda x : -x
        # s = self.get_graph(s)
        # self.add(s)

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
        wt = 1
        surprise = TextMobject("Surprise") 
        text = TextMobject("Let's practice reading payoffs.").to_edge(UL, buff=1)
        # self.play(Write(text))
        # self.wait()
        # self.play(FadeOut(text))

        self.play(ShowCreation(c_short_5))
        self.wait(wt)
        self.play(Write(call_short.to_edge(LEFT, buff=1)))
        self.wait(wt)
        self.play(FadeOut(call_short))
        self.play(FadeOut(c_short_5))
        self.wait(wt)

        self.play(ShowCreation(f_long_5))
        self.wait(wt)
        self.play(Write(forward_long.to_edge(LEFT, buff=1)))
        self.wait(wt)
        self.play(FadeOut(forward_long))
        self.play(FadeOut(f_long_5))
        self.wait(wt)

        self.play(ShowCreation(s_long))
        self.wait(wt+8)
        self.play(Write(asset_long.to_edge(LEFT, buff=1)))
        #self.play(Write(surprise))
        self.wait(wt)
        #self.play(FadeOut(surprise))
        self.play(FadeOut(asset_long))
        self.play(FadeOut(s_long))
        self.wait(wt)

        self.play(ShowCreation(p_long_5))
        self.wait(wt)
        self.play(Write(put_long.to_edge(LEFT, buff=1)))
        self.wait(wt)
        self.play(FadeOut(put_long))
        self.play(FadeOut(p_long_5))
        self.wait(wt)

        self.play(ShowCreation(p_short_5))
        self.wait(wt)
        self.play(Write(put_short.to_edge(LEFT, buff=1)))
        self.wait(wt)
        self.play(FadeOut(put_short))
        self.play(FadeOut(p_short_5))
        self.wait(wt)

        self.play(ShowCreation(m_short_5))
        self.play(Write(money_short.to_edge(LEFT, buff=1)))
        self.wait(wt)
        self.play(FadeOut(money_short))
        self.play(FadeOut(m_short_5))
        self.wait(wt)

        # text = TextMobject("It is a showtime!").to_edge(UL, buff=1)
        # self.play(Write(text))
        # self.wait()
        # self.play(FadeOut(text))

        group = VGroup(call_long, put_short).arrange_submobjects(DOWN).to_edge(LEFT, buff=1)
        self.play(Write(group))
        self.wait(wt)
        self.play(ShowCreation(c_long_5))
        self.play(ShowCreation(p_short_5))
        self.wait(wt)
        self.play(Transform(group, forward_long))
        self.add(f_long_5)
        self.play(FadeOut(c_long_5), FadeOut(p_short_5))
        self.wait(wt)
        self.play(FadeOut(f_long_5), FadeOut(group))
        self.wait(wt)

        self.play(ShowCreation(f_long_5))
        self.wait(wt)
        self.play(Write(forward_long))
        self.wait(wt)
        self.play(Transform(f_long_5.copy(), s_long), Transform(f_long_5.copy(), m_short_5))
        self.wait(wt)
        self.play(FadeOut(f_long_5))
        self.wait(wt)






