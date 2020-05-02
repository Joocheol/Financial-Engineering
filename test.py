from manimlib.imports import *

class abc(Scene):
	def construct(self):
		a = TexMobject("abc", height=0.2, width=1.2)

		self.play(Write(a))
