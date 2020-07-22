## 2차원 배열에 관한 문제
import itertools
arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]	

arr1 = list(itertools.chain(*arr))
## 2차원 배열 --> 1차원 배열로 chain
arr1.sort()

k = 4

result = arr1[k-1]


print(result)