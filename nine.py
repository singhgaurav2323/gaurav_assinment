
class circle:

	def __init__(self,rad):
		self.rad=rad
	def area(self):
		 return 3.14 * self * self

a=int(input())
c=circle(a)

print(circle.area(2))

