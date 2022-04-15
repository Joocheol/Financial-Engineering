from manimlib.imports import *

class aritmetik2(Scene):
    def construct(self):
        skouer_digomp = Tex(
            "3960",
            "=",
            "2",
            "\\times",
            "2",
            "\\times",
            "2",
            "\\times",
            "3",
            "\\times",
            "3",
            "\\times",
            "5",
            "\\times",
            "11"
        )

        skouer_digomp_echu_simplaet = Tex("2^3", "\\times", "3^2", "\\times", "5", "\\times", "11")

        etre_digomp = [
            Tex("2", "\\times", "1980"),
            Tex("2", "\\times", "990"),
            Tex("2", "\\times", "495"),
            Tex("3", "\\times", "165"),
            Tex("3", "\\times", "55"),
            Tex("5", "\\times", "11"),
        ]

        for i in range(5):
            etre_digomp[i].set_color(RED)

        self.play(Write(skouer_digomp[:2]))
        self.wait()
        self.play(Write(etre_digomp[0].next_to(skouer_digomp[:2])))
        self.wait()


        for i in range(5):
            self.play(etre_digomp[i].set_color, WHITE, run_time=1)
            self.wait()
            self.play(etre_digomp[i][2].set_color, RED, run_time=1)
            self.wait()
            #self.play(ReplacementTransform(etre_digomp[i][2], etre_digomp[i+1].next_to(etre_digomp[i][2], RIGHT, buff=-0.5, aligned_edge=LEFT)))
            self.play(ReplacementTransform(etre_digomp[i][2], etre_digomp[i+1].next_to(etre_digomp[i][2], RIGHT,buff=-0.3, aligned_edge=LEFT)))
            self.wait()

        self.wait(5)