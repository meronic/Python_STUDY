import time
from math import sqrt

k = 4
plist = [2, 3]
start_time = time.time()

while True :
    if len(plist) == 1001 :
        break
    
    for i in range(len(plist)) :
        if k % plist[i] == 0 :
            k += 1
            break
        
        elif plist[i] > sqrt(k) :
            plist.append(k)
            k += 1
            break
    
print(plist[-1])
print('\n', time.time() - start_time)