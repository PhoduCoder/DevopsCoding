#given a sentence 
# write an iterator that 
# loops through the words 
# of the sentence

#This is an improved 
# and more efficient example
# than the previous one
# since we are not creating the list all the time 

# We will move the words list
# creation in the init function instead
# so that we can avoid creating the list everytime


class Sentence():

	def __init__(self, sent):
		self.sentence = sent
		self.index = 0
		self.words_list = self.sentence.split(" ")
	def __iter__(self):
		return self

	def __next__(self ):
		
		if (self.index>=len(self.words_list)):
			raise StopIteration
		
		else:
			current=self.words_list[self.index]
			self.index+=1
			return current



mysentence=Sentence("Gaurav is a good boy")

for word in mysentence:
	print (word)

#print(type(mysentence))
