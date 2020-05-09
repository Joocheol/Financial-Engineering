from manimlib.imports import *

class a20200509_10(Scene):
    def construct(self):
        
        fx = lambda x: x.get_value()**2
        
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))

        x_tex = Integer(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        dot = Dot(radious = x_value.get_value()).add_updater(lambda x: x.move_to(0.1*x_value.get_value()))
        
        self.add(x_tex)
        self.add(dot)
        
        self.play(
            x_value.set_value,30,
            rate_func=linear,
            run_time=10
            )
        self.wait()
