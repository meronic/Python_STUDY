d = [2,2,3,3]
budget = 10

d.sort()

for i in range(len(d)) : 
    if (budget >= d[i]) : 
        budget = budget - d[i]
        d[i] = -1

result = d.count(-1)

