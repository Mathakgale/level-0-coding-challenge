import math 

# considering tringle of side a,b and d

def area (a,b,c):
	s = 0.5*(a+b+c)							#calculates the semi-parimeter
	area = (s*(s-a)*(s-b)*(s-c))**(1/2)		# calculates the area
	return area

area = area(2,3,4)
print(area)