from collections import Counter

def enumerate_example(fruit_list):
	for i, j in enumerate(fruit_list):
		print ("My {} favorite fruit is {}".format(i,j))
	c=Counter(fruit_list)

	for key, values in c.items():
		print ("This fruit {} occured {} times".format(key, values))

if (__name__=="__main__"):
	fav_fruits_list=['Grapes', 'Guava','Pineapple', 'Oranges', 'Grapefruit',] 
	enumerate_example(fav_fruits_list)
