mystr = 'bbaa'

find_str = list(set(mystr)) ##중복 제거 하고 정렬

count_str = []

for i in find_str : 
    count_str.append(mystr.count(i))

dic_str = {}

dic_str.update(zip(find_str, count_str))

dic_min = min(dic_str.values())
dic_max = max(dic_str.values())

answer = []


for key, value in dic_str.items() : 
    if value == dic_max : 
        answer.append(key)

answer.sort()
answer = ''.join(answer)

print(answer)