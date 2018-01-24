import numpy as np
from random import randint

def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    bigList = []
    mid = []
    smallList = []
    for i in list:
        if i == pivot:
            mid.append(i)
        elif i < pivot:
            smallList.append(i)
        else:
            bigList.append(i)
    return (quickSort(smallList) + mid + quickSort(bigList))

def createMatrix(m, minN, maxN):
    matrix = np.arange(m*m).reshape(m, m) #Creates matrix with size 'm'*'m'
    for i in matrix:#gives random values between 'minN' and 'maxN' to the elements in the matrix
        for j in range(len(i)):
            i[j] = randint(minN, maxN)
    print(matrix)
    return matrix

def smallSum(matrix, n):#return the smallest sum of 'n' elements in a matrix
    m = int()
    for i in matrix:#gets value of 'm' from matrix
        m += 1
    diagList = [None]*n
    nSum = int()
    for j in range(m):
        if j >= n:
            diagList = quickSort(diagList)
            if diagList[n - 1] > matrix[j, j]:
                diagList[n - 1] = matrix[j, j]
        elif diagList[j] == None:
            diagList[j] = matrix[j, j]
        elif matrix[j, j] > diagList[j]:
            diagList[j] = matrix[j, j]
    nSum = sum(diagList)
    dia = -1#sets 'dia' to '-1'
    mx = m
    while mx >= n:#gets the diagonals with at least 'n' numbers in one half of the matrix
        dia += 1
        mx -= 1
    diaS = 1
    while diaS <= dia:#verifies the smalles sum of 'n' elements on a diagonal starting at 'diaS' as well as its mirror
        for k in range(m):
            if k >= n:
                diagList = quickSort(diagList)
                if diagList[n - 1] > matrix[k - dia, k]:
                    diagList[n - 1] = matrix[k - dia ,k]
            elif diagList[k] == None:
                diagList[k] = matrix[k - dia ,k]
            elif matrix[k - dia, k] > diagList[k]:
                diagList[k] = matrix[k - dia, k]        
        if sum(diagList) < nSum:
            nSum = sum(diagList)
        for k in range(m):
            if k >= n:
                diagList = quickSort(diagList)
                if diagList[n - 1] > matrix[k, k - dia]:
                    diagList[n - 1] = matrix[k, k - dia]
            elif diagList[k] == None:
                diagList[k] = matrix[k, k - dia]
            elif matrix[k, k - dia] > diagList[k]:
                diagList[k] = matrix[k, k - dia]
        if sum(diagList) < nSum:
            nSum = sum(diagList)
        diaS += 1
    return nSum

if __name__ == '__main__':
    print(smallSum(createMatrix(4, 1, 5), 3))
