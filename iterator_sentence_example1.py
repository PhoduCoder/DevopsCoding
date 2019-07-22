#given a sentence 
# write an iterator that 
# loops through the words 
# of the sentence

class Sentence():

	def __init__(self, sent):
		self.sentence = sent
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self ):
		
		words_list=self.sentence.split(" ")
		if (self.index>=len(words_list)):
			raise StopIteration
		
		else:
			current=words_list[self.index]
			self.index+=1
			return current



mysentence=Sentence("Gaurav is a good boy")

for word in mysentence:
	print (word)

#print(type(mysentence))
