import math 

# considering tringle of side a,b and d

def area (a,b,c):
	s = 0.5*(a+b+c)
	return math.sqrt(s*(s-a)*(s-b)*(s-c))

area = area(2,3,4)
print(area)