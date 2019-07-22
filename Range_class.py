class MyRange():

	def __init__(self, start, end):
		self.value=start
		self.end=end


	def __iter__(self):
		return self

	def __next__(self):
		if self.value<self.end:
			raise StopIteration
		current=self.value
		self.value-=1
		return current

myran=MyRange(25,10)

for num in myran:
	print(num)
