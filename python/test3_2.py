while 1 > 0:
	print("Enter score: ",end="")
	try:
		score = float(input())
	except:
		print("Error,please input a number")
		continue
	if score <= 1.0 and score >=0.9:
		print("A")
	elif score >= 0.8 and score < 0.9:
		print("B")
	else:
		print("Bad number")
		continue