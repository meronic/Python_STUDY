# 코딩테스트 체육복 문제


# 전체 학생의 수
n = 5
# 전체 학생의 번호
n_list = list(range(1,n+1))

# 체육복이 두벌씩 있는 애들
reserve = [3,5]

# 체육복을 도난 당한 학생 리스트
lost = [2,4]

# 왼쪽애가 빌려주는걸로 하자

for i in range(len(lost)) : 
    n_list.remove(lost[i])

result = n_list.copy() # 확실하게 있는 애들

print("확실하게 있는 애들", result)



check_list = [] # 2벌인데 1벌 잃어버린 애들

for check in lost :  
    if check in reserve : 
        check_list.append(check)
        reserve.remove(check)



for i in n_list : 
    if i in reserve and (i-1) in lost : 
        result.append(i-1)
        reserve.remove(i)
        lost.remove(i-1)
        
    if i in reserve and (i+1) in lost : 
        
        result.append(i+1)
        reserve.remove(i)
        lost.remove(i+1)
    
    



sum = result + check_list
sum.sort()

a = list(set(sum))

print(a, len(a))



