
"""
	This function convert any number into hours and minutes
"""
def compute (number):
	hours = 0
	minutes = 0
	while number >= 60:
		hours = hours+1
		number=number-60
	minutes = number

	if minutes == 0 :
		if hours == 1:
			print(f" {hours} hour")
		else:
			print(f" {hours} hours")
	else:
		if hours == 1:
			print(f" {hours} hour, {minutes} minutes")
		else:
			print(f" {hours} hours, {minutes} minutes")



compute(100)
compute(133)
compute(71)
compute(60)

