

def maximum (num1, num2, num3):
	largest  = float('-inf')
	if  largest  < num1:
		largest = num1
	if largest < num2:
		largest = num2
	if largest < num3:
		largest = num3
	return largest


max_number = maximum(33,2,78)
print(max_number)
max_number = maximum(3,22,8)
print(max_number)
max_number = maximum(33,2,7)
print(max_number)
max_number = maximum(-33,2,7)
print(max_number)
max_number = maximum(-33,-2,-7)
print(max_number)
