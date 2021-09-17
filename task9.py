
def find_vowels(word):
	vowels = ['a','e','i','o','u']
	word = word.lower()
	found_vowels = []

	# finds vowels in string
	for i in vowels:
		for j in word:
			if i == j:
				found_vowels.append(i)
				break

	# This section print the results
	print ("Vowels: ",end="")
	count = 0
	for i in found_vowels:
		if count >= len(found_vowels)-1:
			print(f'{i}')
		else:
			print(f"{i}, ",end="")
		count=count+1 
		

find_vowels("Umuzi")
find_vowels("theeeesone")


