array = [1,5,2,6,3,7,4]

command = [[2,5,3],[4,4,1],[1,7,3]]
result = []

for i in range(len(command)) : 
    start = command[i][0]
    end = command[i][1]
    idx = command[i][2]

    split_list = array[start-1:end]
    split_list.sort()

    find = split_list[idx-1]
    result.append(find)


print(result)
