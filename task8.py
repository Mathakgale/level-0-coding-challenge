
def get_min_string(minutes):
	if minutes == 1:
		return f'{minutes} minute'
	elif minutes == 0:
		return''
	return f'{minutes} minutes'

def get_hour_string(hour):
	if hour == 1:
		return f'{hour} hour'
	elif hour == 0:
		return ''
	return f'{hour} hours'

def convert_to_hrs_min (number):
	hours = 0
	minutes = 0
	while number >= 60:
		hours = hours+1
		number=number-60
	minutes = number
	if hours == 0:
		print(get_min_string(minutes))
	else:
		print(f'{get_hour_string(hours)} {get_min_string(minutes)}')



convert_to_hrs_min(100)
convert_to_hrs_min(133)
convert_to_hrs_min(71)
convert_to_hrs_min(60)
convert_to_hrs_min(30)
convert_to_hrs_min(1)
convert_to_hrs_min(61)
convert_to_hrs_min(121)