from manimlib.imports import *

class abc(Scene):
	def construct(self):
		a = Vector()

		self.play(MoveCar(a, RIGHT*3))
