try:
	print("Enter Hours: ",end ="")
	hours = float(input())
	print("Enter Rate: ",end ="")
	rate = float(input())
except:
	print("Error,please enter numeric input")
	quit()
salary = rate * hours
if hours > 40:
	print("pay: ",(40 * rate) + (hours - 40) * 1.5 *rate)
else:
	print("pay: ",salary)