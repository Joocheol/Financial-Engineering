from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))

C_list = [0, 37.8, -17.8, -50]
F_list = [32.0, 100, 0, -58]

class a001(Scene):
    def construct(self):

        C = Matrix(C_list, element_alignment_corner=DOWN)
        F = Matrix(F_list, element_alignment_corner=DOWN)
        C.move_to(LEFT)
        F.next_to(C, RIGHT)

        self.play(Write(C))
        self.play(Write(F))

class a002(GraphScene):

    CONFIG = {
    "x_min" : -100,
    "x_max" : 100,
    "x_tick_frequency": 10,
    "y_min" : -100,
    "y_max" : 120,
    "y_tick_frequency": 10,
    "graph_origin" : ORIGIN,
    "function_color" : RED,
    "axes_color" : GREEN,
    "x_labeled_nums" :range(-100,101,50), 
    #"y_labeled_nums" :range(-10,120,50),    
    }

    def construct(self):
        self.setup_axes(animate=True

            )

        
        for i, j in zip(C_list, F_list):
            point = Dot().move_to(self.coords_to_point(i,j)).set_color(YELLOW)
            self.play(ShowCreation(point))

        #a = self.coords_to_point(10, 20)
        #func_graph=self.get_graph(self.func_to_graph,self.function_color)
        #func_graph2=self.get_graph(self.func_to_graph2)
        #vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        #graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        #graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        #two_pi = TexMobject("x = 2 \\pi")
        #label_coord = self.input_to_graph_point(TAU,func_graph)
        #two_pi.next_to(label_coord,RIGHT+UP)
     
        #self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        #self.play(ShowCreation(vert_line), ShowCreation(graph_lab), 
        #    ShowCreation(graph_lab2),ShowCreation(two_pi))
     
       # point = Dot().move_to(a)
        #self.play(ShowCreation(point))

    def func_to_graph(self,x):
        return np.cos(x)
     
    def func_to_graph2(self,x):
        return np.sin(x)
        
        # grid = []
        # for i in range(25):
        #     grid.append(Grid(1,1, height=0.5, width=0.5))
        #     grid[i].move_to([8*(i-25)/25+4, 3, 0]).scale(0.6)
        #     self.play(ShowCreation(grid[i]), run_time=0.1)

class a003(Scene):
    def construct(self):

        eqn = TexMobject("""
            \\hat{\\beta}_{1} = { {\\sum ( x_i - \\bar{x} ) ( y_i - \\bar{y} ) } 
            \\over { \\sum ( x_i - \\bar{x} )^2  } }
        """)

        self.play(Write(eqn))

class a004(Scene):
    def construct(self):

        text0 = TextMobject("$x$")
        text0.move_to(UP*3)
        self.play(Write(text0))

        text1 = TextMobject("$y = f(x)$")
        text1
        self.play(Write(text1))

        text2 = TextMobject("$y$")
        text2.move_to(DOWN*3)
        self.play(Write(text2))


        r = 1
        top_node = 1
        up_node = 15
        down_node = 3

        layer1 = []
        for i in range(up_node):
            layer1.append(Circle(radius=r))
            layer1[i].move_to([0.5*(i-(up_node-1)/2.), 0, 0]).scale(0.2).set_color(WHITE)
        #    self.play(ShowCreation(layer1[i]), run_time=0.1)
        layer1_g = VGroup(*layer1)
        self.play(Transform(text1, layer1_g))
        

        layer0 = []
        for i in range(top_node):
            layer0.append(Circle(radius=r))
            layer0[i].move_to([0.5*(i-(top_node-1)/2.), 3, 0]).scale(0.2).set_color(WHITE)
            self.play(ShowCreation(layer0[i]), run_time=0.1)

        


        lines = []
        for i in range(top_node):
            for j in range(up_node):
                s = layer0[i].get_center() # grid[i].get_center()
                e = layer1[j].get_center()
                lines.append(Line(s, e).set_stroke(width=0.5))

        lines_g = VGroup(*lines)
        self.play(ShowCreation(lines_g))
           

        layer2 = []
        for i in range(down_node):
            layer2.append(Circle(radius=r))
            layer2[i].move_to([0.5*(i-(down_node-1)/2.), -3, 0]).scale(0.2).set_color(WHITE)
            self.play(ShowCreation(layer2[i]), run_time=0.1)

        lines = []
        for i in range(up_node):
            for j in range(down_node):
                s = layer1[i].get_center()
                e = layer2[j].get_center()
                lines.append(Line(s, e).set_stroke(width=0.5))

        lines_g = VGroup(*lines)
        self.play(ShowCreation(lines_g))

        layer2_g = VGroup(*layer2)

        down_node = 1

        layer2 = []
        for i in range(down_node):
            layer2.append(Circle(radius=r))
            layer2[i].move_to([0.5*(i-(down_node-1)/2.), -3, 0]).scale(0.2).set_color(WHITE)
        #    self.play(ShowCreation(layer2[i]), run_time=0.1)

        layer2_g2 = VGroup(*layer2)
        self.play(Transform(layer2_g, layer2_g2))

class a005(Scene):
    def construct(self):

        x = TexMobject("x")
        f_1_x = TexMobject("f_1 (x)", "=", "w_{1,1}", "x", "+", "b_{1,1}")
        f_2_x = TexMobject("f_2 (x)", "=", "w_{1,2}", "x", "+", "b_{1,2}")
        y_hat = TexMobject("\\hat{y}", "=", "w_{2,1}", "f_1", "+", 
            "w_{2,2}", "f_2", "+", "b_{2,1}" )

        x.move_to(UP*3)
        f_1_x.move_to(LEFT*3)
        f_2_x.move_to(RIGHT*3)
        y_hat.move_to(DOWN*3)

        self.play(Write(x))
        self.play(Transform(x.copy(), f_1_x[3]), Transform(x.copy(), f_2_x[3]))
        self.wait(2)
        self.play(Write(VGroup(f_1_x, f_2_x)))
        self.wait(2)
        self.play(Transform(f_1_x[0].copy(), y_hat[3]), Transform(f_2_x[0].copy(), y_hat[6]))
        self.wait(2)
        self.play(Write(y_hat))
        self.wait()
        

