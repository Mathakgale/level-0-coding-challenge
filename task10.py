"""
	the function takes two strings as input, and outputs the common characters/letters 
	that they share.
"""
def common_letters(word_1, word_2):
	word_1 = word_1.lower()
	word_2 = word_2.lower()
	print ("Common letters: ",end="")
	for i in word_1:
		for j in word_2:
			if i == j:
				print(i+" ",end="")
				break
	print()


common_letters ("house", "computers")


