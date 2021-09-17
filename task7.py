
def celsius_to_fahrenhiet(temp):
	return (9/5)*temp +32

def fahrenhiet_to_celsius (temp):
	return (temp-32)*(5/9)

celsius = fahrenhiet_to_celsius (34)
print (f"in celsius {celsius}")

fahrenhiet = celsius_to_fahrenhiet(celsius)
print (f"in fahrenhiet {fahrenhiet}")