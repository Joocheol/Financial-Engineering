from manimlib.imports import *

class a20200526_15(Scene):
	def construct(self):
		
		text = TextMobject("The put-call parity")
		self.play(Write(text))
		self.wait(30)