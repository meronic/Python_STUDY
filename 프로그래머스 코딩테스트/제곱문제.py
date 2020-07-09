import math

n = 121

sqrt_n = math.sqrt(n)

check = math.modf(sqrt_n)[0]

find_number = int(math.modf(sqrt_n)[1])

answer = 0

if check == 0 : 
    answer = math.pow((find_number + 1),2)

else : answer = -1







