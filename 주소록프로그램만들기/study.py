answers = [1,3,2,4,2]

num1_score = 0
num2_score = 0
num3_score = 0

num1 = []
num2 = []
num3 = []

for i in range(2000) :
    num1.extend([1,2,3,4,5])



for i in range(1000) : 
    num2.extend([2,1,2,2,2,3,2,4,2,5])


for i in range(1000) : 
    num3.extend([3,3,1,1,2,2,4,4,5,5])

for i in range(len(answers)) : 

    if answers[i] == num1[i] :
        num1_score += 1

    elif answers[i] == num2[i] : 
        num2_score += 1

    elif answers[i] == num3[i] : 
        num3_score += 1

scores = [num1_score, num2_score, num3_score]

max_score = max(scores)

result = []
answer = []
if scores.count(max_score) == 1 : 
    if max_score == num1_score :
        result.append(1)

    elif max_score == num2_score : 
        result.append(2)

    elif max_score == num3_score : 
        result.append(3)

elif scores.count(max_score) == 2 : 
    if max_score == num1_score :
        result.append(1)

    elif max_score == num2_score : 
        result.append(2)

    elif max_score == num3_score : 
        result.append(3)

    elif scores.count(max_score) == 3 : 
        result.append(1)
        result.append(2)
        result.append(3)

answer = result
