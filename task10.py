
def common_letters(word_1, word_2):
"""
	the function takes two strings as input, and outputs the common characters/letters 
	that they share.
"""
	word_1 = word_1.lower()
	word_2 = word_2.lower()
	found_chars = []
	#This section finds the matching letters
	for i in word_1:
		for j in word_2:
			if i == j:
				found_chars.append(i)
				break
	# This section print the results
	print ("Common letters: ",end="")
	count = 0
	for i in found_chars:
		if count >= len(found_chars)-1:
			print(f'{i}')
		else:
			print(f"{i}, ",end="")
		count=count+1 


common_letters ("house", "computers")


