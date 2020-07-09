# 번호순으로 체격이 매겨짐 앞뒤로 1번째밖에 빌려주지 못함
# 3번이 없다면 2,4번만이 빌려 줄 수 있음

n = 5
lost = [2,4]
reserve = [3]
# 4

total = list(range(1,n+1))
result = list(range(1,n+1))

print("체육복 잃어버린 불쌍한 놈들",lost)
print("두벌씩 갖고 댕기는 애들",reserve)


# 일단 전체 - 잃어버린 애들
for i in total : 
	if i in lost : 
		result.remove(i)


print("일단 확실하게 있는 애들  : ", result)

# 있는데 털린애들
for i in range(len(lost)) : 
	if lost[i] in reserve : 
		reserve.remove(lost[i])
print("두벌중에서 한벌 털린 애들", reserve)
size = len(lost)
# 체육복 빌려주기
for i in range(0,size) : 
	if reserve.count(lost[0] - 1) == 1 or reserve.count(lost[0] + 1) == 1:
		result.append(lost[0])
		lost.remove(lost[i])
		



a = set(result)
print(result)
print(a)
