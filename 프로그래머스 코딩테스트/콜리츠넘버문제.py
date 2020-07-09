global count 
count = 0

def Colliatz(n) : 
    global count
    if (n == 1) :
        if (count > 500) :
            count = -1
            return count 

        return count

    elif (n%2 == 0) :
        n = n/2
        count += 1
        return Colliatz(n)


    elif (n%2 != 0) : 
        n = n*3+1 
        count += 1
        return Colliatz(n)



print(Colliatz(626331))




