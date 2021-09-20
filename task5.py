
# considering tringle of side a,b and d

def area (a,b,c):
	semi_parimeter = 0.5*(a+b+c)						
	area = (semi_parimeter*(semi_parimeter-a)*(semi_parimeter-b)*(semi_parimeter-c))**(1/2)		
	return area

area = area(2,3,4)
print(area)