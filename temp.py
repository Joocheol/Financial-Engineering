from manimlib.imports import *

class ShiftFour2(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	def construct(self):
		self.camera_frame.scale(1.3)
		a=Dot(color=RED)
		b=Dot(color=BLUE)
		c=Dot(color=RED)
		d=Dot(color=BLUE)

		scale=3

		a.scale(scale)
		b.scale(scale)
		c.scale(scale)
		d.scale(scale)

		a.next_to(b,LEFT,1)
		c.next_to(b,RIGHT,1)
		d.next_to(c,RIGHT,1)

		s_dots=VGroup(a,b,c,d)

		s_dots.move_to(ORIGIN)

		s_dots.shift(UP*3)

		self.play(ShowCreation(s_dots))

		self.wait()

		arrows=[]

		dots=[]

		def shift_down(a,b,c,d):
			scale=3
			a_new=Dot(color=d.get_color())
			b_new=Dot(color=a.get_color())
			c_new=Dot(color=b.get_color())
			d_new=Dot(color=c.get_color())

			a_new.scale(3)
			b_new.scale(3)
			c_new.scale(3)
			d_new.scale(3)

			a_new.move_to(a.get_center()+DOWN*1.8)
			b_new.move_to(b.get_center()+DOWN*1.8)
			c_new.move_to(c.get_center()+DOWN*1.8)
			d_new.move_to(d.get_center()+DOWN*1.8)

			arr=TextMobject("$$\\rightarrow$$")
			arr.scale(1.9)
			arr.rotate(about_point=arr.get_center(),angle=-PI/2)
			f_g=VGroup(b,c,b_new,c_new)
			arr.move_to(f_g.get_center())

			arrows.append(arr)

			dots.append(a_new)
			dots.append(b_new)
			dots.append(c_new)
			dots.append(d_new)

			self.play(ShowCreation(arr))
			self.play(
				ShowCreation(a_new),
				ShowCreation(b_new),
				ShowCreation(c_new),
				ShowCreation(d_new)
				)


		shift_down(a,b,c,d)

		self.wait()

		shift_down(dots[0],dots[1],dots[2],dots[3])

		self.wait()

		self.wait(2)

		self.play(
			FadeOut(dots[4]),
			FadeOut(dots[5]),
			FadeOut(dots[6]),
			FadeOut(dots[7]),
			FadeOut(arrows[1])
			)

		self.wait(2)

		self.play(
			FadeOut(dots[0]),
			FadeOut(dots[1]),
			FadeOut(dots[2]),
			FadeOut(dots[3]),
			FadeOut(arrows[0])
			)
		self.play(ApplyMethod(s_dots.move_to,ORIGIN))
		self.play(ApplyMethod(self.camera_frame.scale,0.5))

		self.wait(2)

		f_g=VGroup(a,b)

		buff=0.2
		box1=Rectangle(height=a.get_height()+buff,width=f_g.get_width()+buff,stroke_color=BLUE)
		box1.move_to(f_g.get_center())

		f_g2=VGroup(c,d)

		box2=Rectangle(height=a.get_height()+buff,width=f_g.get_width()+buff,stroke_color=BLUE)
		box2.move_to(f_g2.get_center())

		self.play(ShowCreation(box1))
		self.wait()
		self.play(ShowCreation(box2))

		self.wait(2)

		g1=VGroup(a,b,box1)
		g2=VGroup(c,d,box2)

		g=VGroup(g1,g2)

		angle=ValueTracker(0)

		dist=np.abs(g2.get_center())

		self.play(
			ApplyMethod(g1.move_to,g2.get_center()),
			ApplyMethod(g2.move_to,g1.get_center()),
			)

		self.wait(2)