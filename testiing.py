class Geek:
	
	# constructor
	def __init__(self, name, age):
		# public data mambers
		self.geekName = name
		self.geekAge = age

	# public member function	
	def displayAge(self):
		print("Age: ", self.geekAge)