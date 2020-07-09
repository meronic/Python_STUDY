from itertools import permutations

numbers = [3, 30, 34, 5, 9]

# 일단 오름차순으로 정렬
numbers.sort()

# 가능한 조합의 수 모두 만들어서 리스트에 저장
list_p = list(permutations(numbers))

# 만든 수들을 저장할 리스트
sum_list = []

print(numbers,"로 만들 수 있는 모든 수")
for i in range(len(list_p)) : 
	str1 = ''
	for j in range(len(list_p[i])) : 
		str1 += str(list_p[i][j])
	sum_list.append(int(str1)) # 정수형으로 저장

print(sum_list) # 만든 수들의 리스트 찍어보기 

result = max(sum_list) #여기서 가장 큰 수 찾기

print("max number :",result)



