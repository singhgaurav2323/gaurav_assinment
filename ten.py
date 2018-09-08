
class String():
	def getstring (self):
		self.main=input("enter string :")
	def printstring(self):
		return(self.main)

def test():
	ace=String()
	ace.getstring()
	b=ace.printstring()
	print(b.upper())

test()
