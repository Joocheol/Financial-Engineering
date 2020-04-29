from manimlib.imports import *
import random

class a001(Scene):
	def construct(self):

		c = Circle()
		self.add(c)

		for i in range(100):
			self.play(Transform(c, 
				c.move_to([random.uniform(-5,5), random.uniform(-3,3), 0])),
				run_time = .1 )

