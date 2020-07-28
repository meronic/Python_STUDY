# kakao 인형뽑기 문제 개노가다
import numpy

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


for i in range(len(board)) : 
    view = list(map(str, board[i]))
    view = '  '.join(view)
    print(view)

trans_board = numpy.transpose(board)

check_board = []
print(trans_board)

for i in range(len(trans_board)) : 
    temp = list(trans_board[i])
    count = temp.count(0)
    for j in range(count) : 
        temp.remove(0)
        
    check_board.append(temp)
    

print(check_board)

room = []

for i in moves : 
    temp = check_board[i-1]
    if len(temp) == 0 :
        continue
    room.append(temp[0])
    print(temp)
    del check_board[i-1][0]


print('result', room)
count = 0

result = room.copy()

count = 0

def fun(array) :
    global count
    for i in range(1, len(array)) : 
        if array[i] == array[i-1] : 
            count +=2
            del array[i-1:i+1]
            return fun(array)

fun(result)

print(count)

