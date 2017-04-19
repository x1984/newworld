def printscor(a):
	if a <= 1.0 and a >=0.9:
		print("A")
	elif a >= 0.8 and a < 0.9:
		print("B")
	else:
		print("Bad number")
while 1 > 0:
	print("Enter score: ",end="")
	try:
		score = float(input())
	except:
		print("Error,please input a number")
		continue
	printscor(score)