
"""
	This function convert any number into hours and minutes
"""
def compute (number):
	hours = 0
	minutes = 0
	while number > 60:
		hours = hours+1
		number=number-60
	minutes = number

	print(f" {hours} hours and {minutes} minutes")



compute(100)
compute(133)
compute(71)