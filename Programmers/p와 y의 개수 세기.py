# 문자열에서 p와 y의 개수 세기

import collections 

ex = 'Pyy'

a = list(ex.lower())

b = collections.Counter(a)
print(b)

p_count = b['p']
y_count = b['y']

if p_count == y_count : 
    answer = True
elif p_count != y_count : 
    answer = False

print(answer)