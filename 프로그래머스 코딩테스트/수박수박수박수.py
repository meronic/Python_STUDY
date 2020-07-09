su = '수'
bak = '박'
result = ''
n = 11

for i in range(1,n+1) :
	if i == 1 : 
		result += su 
	elif i == 2 : 
		result += bak

	elif i%2 != 0 : 
		result += su

	elif i%2 == 0 :
		result += bak

print(result)




