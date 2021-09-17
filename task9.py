
def find_vowels(word):
	vowels = ['a','e','i','o','u']
	word = word.lower()
	found_vowels = []
	# finds vowels in string
	print ("Vowels : ",end="")
	for i in vowels:
		for j in word:
			if i == j:
				print(i+" ",end="")
				break
	print()


find_vowels("Umuzi")
find_vowels("theeeesone")


