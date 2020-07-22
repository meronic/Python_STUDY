import operator

n = 5 # 전체 스테이지의 개수
stage_list = list(range(1,6)) # 스테이지의 방 만들기
fail_probability = [0]*(len(stage_list)) # 실패율 0으로 초기화
stages = [1, 2, 2, 2, 3, 3, 4, 6]	# 못깬 스테이지


total_user = len(stages) # 이용하는 유저의 수

end_stage = n + 1 # 전부 다 클리어한 유저의 스테이지

#실패율 = 클리어하지 못한 플레이어의 수 /
#         스테이지에 도달한 플레이어 수

stages.sort() # 일단 정렬

info_dic = {}
info_dic.update(zip(stage_list, fail_probability))

for i in range(1, (n+1)) : 
    if i in stages : 
        info_dic[i] = stages.count(i) / len(stages)
        count = stages.count(i)
        for j in range(count) : 
            stages.remove(i)

print(info_dic)

fail_probability = list(info_dic.values()) # 실패율 
fail_probability.sort(reverse=True)

print(fail_probability)


answer = []

count = 0
for i in fail_probability : 
    if i in info_dic.values() : 
        answer.append(info_dic.key(i))
    
    

