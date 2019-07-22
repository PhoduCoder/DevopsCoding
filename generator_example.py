def generator_example_range(start, end):
	current = start
	while (current < end):
		yield current
		current+=1

nums=generator_example_range(5,30)

print(type(nums))

print(next(nums))

print (nums.__next__())

for i in nums:
	print (i)
