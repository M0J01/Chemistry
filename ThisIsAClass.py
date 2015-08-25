##This is a Class

class Hero:
	def __init__(self,name):
		self.name = name
		self.health = 100
		
	def eat(self, food):
		if (food == 'apple'):
			self.health += 100
		elif (food == 'ham'):
			self.health += 20
		else:
			self.health -= 5
			

Bob = Hero("Bob")
print Bob.name
print Bob.health
Bob.eat(10)
print Bob.health
Bob.eat('apple')
print Bob.health









# class Ph:
	# def __init__(self):
		# self.y = 5
		# self.printHam()
	# def printHam(self):
		# print "ham"
	# food = 'steak'
# x = Ph()
# x.printHam()
# print x.food
# print x.y
