from manimlib.imports import *

class a20200529_10(GraphScene):


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