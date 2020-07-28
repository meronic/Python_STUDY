# kakao 비밀지도 코딩테스트 문제

n = 6

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]


list1 = []
list2 = []
answer = []



for i in arr1 : 
    b = format(i, 'b')
    b = b.rjust(n, '0')
    list1.append(b)

for j in arr2 : 
    b = format(j, 'b')
    b = b.rjust(n, '0')
    list2.append(b)


print(list1)
print(list2)

sum = 0

for k in range(len(list1)) : 
    sum = int(list1[k]) + int(list2[k])
    sum = str(sum).replace('2','1')
    sum = sum.rjust(n, '0')
    answer.append(sum)

print(answer)

for i in range(len(answer)) : 
    answer[i] = answer[i].replace('1', '#')
    answer[i] = answer[i].replace('0', ' ')

print(answer)



result = ' \r'.join(answer)
result = result.replace('1', '# ')
result = result.replace('0', '  ')

print(result)

result = list(result)


