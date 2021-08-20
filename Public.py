class Geek:
	
	# constructor
	def __init__(self, name, age):
		# public data mambers
		self.geekName = name
		self.geekAge = age

	# public member function	
	def displayAge(self):
		print("Age: ", self.geekAge)


obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

obj.displayAge()

add a+b
