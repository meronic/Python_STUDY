n = 6
end = 0
while (end == 0) : 
	if (n%2 == 0) :
		n = n/2

	elif (n%2 != 0) : 
		n = n*3+1

	elif (n == 1) : 
		print("finish!!")
		end = 1
		break;