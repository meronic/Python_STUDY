def prime(n) : 
	count = 0
	
	if n == 2 : 
		return 2	
	
	for i in range(2,n) : 
		rest = n % i
		if rest == 0 :
			count += 1
			continue
	if count == 0 :
		return n

c = int(input("Enter the count number : "))
n_list = []
j = 2
while True : 
	n_list.append(prime(j))
	try : 
		n_list.remove(None)
	except : 
		pass
	

	if len(n_list) == c : 
		#print(n_list)
		break
	j += 1
	
print("last prime number is : ", n_list[-1])
print("len[prime number list] : ", len(n_list))
