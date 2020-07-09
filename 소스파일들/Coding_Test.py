# 소수 구하는 프로그램

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

print(prime(10))