from manimlib.imports import *
import numpy as np



class a20200512_20(GraphScene):

    CONFIG = {
        "y_max" : 1.2,
        "y_min" : 0,
        "x_min" : -16,
        "x_max" : 16,
        "graph_origin": [0,-3,0]
    }

    def construct(self):

        self.setup_axes()
        g = lambda x : 1/(1+np.exp(-x))
        gg = self.get_graph(g)
        self.add(gg)
        
        
        
        fx = lambda x: 1/(1+np.exp(-x.get_value()))
        
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value(), num_decimal_places = 10).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = TexMobject("x = ")
        fx_label = TexMobject("f(x) = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(1)
        VGroup(x_tex, fx_tex).arrange_submobjects(DOWN)
        # Align labels and numbers
        x_label.next_to(x_tex,LEFT, buff=0.3,)
        fx_label.next_to(fx_tex,LEFT, buff=0.3,)

        pt = Dot().add_updater(
            lambda v: v.move_to( self.coords_to_point ( x_value.get_value(), fx(x_value) ) ) 
        )
        
        self.add(pt)

        self.add(group.to_edge(UL, buff=1))
        self.wait()
        self.play(
            x_value.set_value,15,
            rate_func=linear,
            run_time=5
            )
        self.wait()
        self.play(
            x_value.set_value,-15,
            rate_func=linear,
            run_time=5
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=5
            )
        self.wait()

        string = r"""
            f(x) = {{1} \over {1 + e^{-x}}}
        """
        string = string.split()
        f_1 = TexMobject(*string)
        f_1.to_edge(LEFT, buff=1)

        self.play(Write(f_1))
        self.wait()
