#프로그래머스 코딩테스트 모의고사

a = [1,2,3,4,5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answer = [1, 3, 2, 4]

a_score = 0
b_score = 0
c_score = 0



for i in range(len(answer)) : 
    if answer[i] == a[i % len(a)] : a_score += 1
    if answer[i] == b[i % len(b)] : b_score += 1
    if answer[i] == c[i] % len(c) : c_score += 1

result = {1 : a_score, 2 : b_score, 3 : c_score}
print(result)

dic_max = max(result.values())

answer = []


for key, value in result.items() : 
    if value == dic_max : 
        answer.append(key)

print(answer)
