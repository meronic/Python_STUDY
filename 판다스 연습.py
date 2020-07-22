import pandas as pd
import numpy as np

# values = np.array(range(20)).reshape((5,4))
# index = ['a','b','c','d','e']
# columns = ['!','@','#','%']

# df = pd.DataFrame(values, index=index, columns=columns)

# data = [
#     ['1000', 'Steve', 90.72], 
#     ['1001', 'James', 78.09], 
#     ['1002', 'Doyeon', 98.43], 
#     ['1003', 'Jane', 64.19], 
#     ['1004', 'Pilwoong', 81.30],
#     ['1005', 'Tony', 99.14],
# ]

# df = pd.DataFrame(data)

# print(df)
# print(df.index)
# print(df.values)
# print(df.columns)

# df = pd.DataFrame(data, columns = ['number','name','score'])

# data = { '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
# '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
#          '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

# df = pd.DataFrame(data)

# print(df,end = '\n\n')

# # # print(df.head(3)) # 앞의 3개의 데이터
# # # print(df.tail(3)) # 뒤의 3개의 데이터

# # print(df['학번']) # 학번이라는 열의 데이터 전부 가져오기

# print(df['학번'].values_counts())

df = pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]}, index = [1,2,3])

print(df, end = '\n\n')

print(df['a'])
print(df[['a']])

draw = df.plot()

print(draw)