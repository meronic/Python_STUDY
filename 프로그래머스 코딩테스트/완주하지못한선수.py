import collections

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['mislav', 'stanko', 'ana']

# 일단 정렬 해보자
participant.sort()
completion.sort()

# 중복이 아닌 애가 못들어왔을때

set_participant = set(participant)
set_completion = set(completion)

# p > c

if set_participant == set_completion : 
	count_p = collections.Counter(participant)
	count_c = collections.Counter(completion)
	sub_count = count_p - count_c
	result = list(sub_count.elements())[0]
	
else : result = list(set_participant.difference(set_completion))[0] # 둘의 차집함

print(set_participant)
print(set_completion)
print(result)

#collections의 중요성 유틸리티를 활용하자..



