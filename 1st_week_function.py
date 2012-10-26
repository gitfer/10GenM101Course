fruit = ["orange", "apple", "kiwi", "apple"]

def analyze(fruit):
	count = {}
	for item in fruit:
		if item in count:
			count[item] += 1
		else:
			count[item] = 1
	return count


counts = analyze(fruit)
print counts
