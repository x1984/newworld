def salary(rate,hours):
	if hours > 40:
		return (40 * rate) + (hours - 40) * 1.5 *rate
	else:
		return rate * hours
try:
	print("Enter Hours: ",end ="")
	hours = float(input())
	print("Enter Rate: ",end ="")
	rate = float(input())
except:
	print("Error,please enter numeric input")
	quit()
print(salary(rate,hours))
