import numpy as np
from random import randint

def right(matrix, i, j, curN): #check connections to the right of a given element    
    try:        
        if matrix[i, j] == 0:            
            return 0        
        elif matrix[i, j] == matrix[i, j+1]:            
            matrix[i, j] = 0
            r = 1 + right(matrix, i, j+1, curN)
            l = 1 + left(matrix, i, j+1, curN)
            u = 1 + up(matrix, i, j+1, curN)
            d = 1 + down(matrix, i, j+1, curN)            
            matrix[i,j] = curN            
            return max(r, l, u, d)        
        else:            
            return 0        
    except IndexError:        
        return 0

def left(matrix, i, j, curN):#check connections to the left of a given element    
    try:        
        if matrix[i, j] == 0:            
            return 0        
        elif matrix[i, j] == matrix[i, j-1]:            
            matrix[i, j] = 0
            r = 1 + right(matrix, i, j-1, curN)
            l = 1 + left(matrix, i, j-1, curN)
            u = 1 + up(matrix, i, j-1, curN)
            d = 1 + down(matrix, i, j-1, curN)
            matrix[i,j] = curN            
            return max(r, l, u, d)
        else:            
            return 0
    except IndexError:        
        return 0

def up(matrix, i, j, curN):#check connections on top of a given element    
    try:        
        if matrix[i, j] == 0:            
            return 0        
        elif matrix[i, j] == matrix[i-1, j]:            
            matrix[i, j] = 0
            r = 1 + right(matrix, i-1, j, curN)
            l = 1 + left(matrix, i-1, j, curN)
            u = 1 + up(matrix, i-1, j, curN)
            d = 1 + down(matrix, i-1, j, curN)
            matrix[i,j] = curN            
            return max(r, l, u, d)
        else:            
            return 0
    except IndexError:
        return 0

def down(matrix, i, j, curN):#check connections bellow a given element    
    try:        
        if matrix[i, j] == 0:            
            return 0        
        elif matrix[i, j] == matrix[i+1, j]:            
            matrix[i, j] = 0
            r = 1 + right(matrix, i+1, j, curN)
            l = 1 + left(matrix, i+1, j, curN)
            u = 1 + up(matrix, i+1, j, curN)
            d = 1 + down(matrix, i+1, j, curN)
            matrix[i,j] = curN            
            return max(r, l, u, d)
        else:            
            return 0
    except IndexError:        
        return 0

def createMatrix(m, n):
    matrix = np.arange(m*n).reshape(m, n) #Creates matrix with size m*n
    #Changes the numbers in the matrix to random numbers from 1 to 9
    for i in matrix: 
        for j in range(len(i)):
            i[j] = randint(1,9)
    return matrix

def connect(m, n):# runs program returning answer as a tuple
    try:        
        curN = 0
        long = 1
        maxLong = 1
        maxNum = []
        matrix = createMatrix(m,n)#np.matrix([matrix here])
        for i in range(m):
            for j in range(n):            
                curN = matrix[i, j]
                r = long + right(matrix, i, j, curN)
                d = long + down(matrix, i, j, curN)
                if max(r, d) == maxLong:
                    if curN not in maxNum:
                        maxNum.append(curN)
                        maxLong = max(r,  d)
                if max(r, d) > maxLong:
                    maxNum = []
                    maxNum.append(curN)
                    maxLong = max(r, d)        
        return maxLong, maxNum
    except (ValueError, TypeError):        
        return 'One of the values is not an Int.'            
    
def start(m, n): #starts program returning answer as a string    
    funRet = connect(m, n)
    returnLen = len(funRet[1])
    maxNum = str()    
    for i in range(returnLen):        
        if i < returnLen-2:            
            maxNum =  maxNum + str(funRet[1][i]) + ', '
        elif i < returnLen-1:            
            maxNum =  maxNum + str(funRet[1][i]) + ' and '
        else:            
            maxNum =  maxNum + str(funRet[1][i])           
    return 'The size of the biggest set is ' + str(funRet[0]) + ' and the colour is whichever colour you represented by ' + maxNum + '.'

if __name__ == '__main__':
    print(start(6, 4))
