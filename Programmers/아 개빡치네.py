import time
# trangle number

count = 100 # 몇번째까지 삼각수를 나열 할 것인가


for n in range(1,count+1) :
# n번째 삼각수 구하기

	t_number = 0
	rest = []

	for i in range(1,n+1) : 
		t_number += i

	for i in range(1,t_number+1) : 
		if t_number%i == 0 :
			rest.append(i)

	print(n,"번째 삼각수 ",t_number)
	print(n,"번째 삼각수의 약수들 ",rest,end='\n\n')




