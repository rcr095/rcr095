'''Creates a tower of cubes with ascending order.'''

def checkDupl(cubes):
    '''
    Removes a cube of colour 'X' and size 'Z' in case: x - y >= 2
    - x being the sum of all the cubes of colour 'X' and size 'Z' and y all the other cubes of size 'Z'
    Removes the smallest cube of colour 'X' in case: x - y >= 2
    - x being a single colour and y the sum of all the other colours in the list
    '''
    cubes = sortCubes(cubes)
    for x in range(len(cubes)):
        curCol = cubes[x][0]
        curCnt = 0
        othCnt = 0
        for y in range(len(cubes)):
            if cubes[x][0] == cubes[y][0]:
                curCnt += 1
            else:
                othCnt += 1
        if curCnt - othCnt >= 2:
            newList = []
            for cube in reversed(cubes):
                if cube[0] == curCol:
                    curCol = None
                else:
                    newList.append(cube)
            return checkDupl(newList)
    for i in range(len(cubes)):
        curCub = cubes[i]
        curCnt = 0
        othCnt = 0
        for j in range(len(cubes)):
            if cubes[i][1] == cubes[j][1]:
                if cubes[i][0] == cubes[j][0]:
                    curCnt += 1
                else:
                    othCnt += 1
        if curCnt - othCnt >= 2:
            newList = []
            for cube in cubes:
                if cube == curCub:
                    curCub = None
                else:
                    newList.append(cube)
            return checkDupl(newList)
    return cubes
                    
def sortCubes(cubes):#uses a quicksort like function to sort a list of cubes by their size
    if len(cubes) <= 1:
        return cubes
    bigCubes = None
    smallCubes = []
    for cube in cubes:
        if bigCubes == None:
            bigCubes = [cube]
        elif cube[1] > bigCubes[0][1]:
            smallCubes += bigCubes
            bigCubes = [cube]
        elif cube[1] == bigCubes[0][1]:
            bigCubes += [cube]
        else:
            smallCubes += [cube]
    return bigCubes + sortCubes(smallCubes)

def checkLine(cubes):#check if a solution is possible
    prev = [('#', 0)]
    for cube in cubes:
        if cube[0] != prev[0]:
            prev = cube
        else:
            return False
    return True

def pileSort(cubes):#create a solution
    cubes = checkDupl(cubes)
    cubes = sortCubes(cubes)   
    for i in range(1, len(cubes)):
        if cubes[i] == cubes[i - 1]:
            s = i
            while s < len(cubes) and cubes[i][1] == cubes[s][1]:
                if cubes[s][0] != cubes[i][0]:
                    temp = cubes[s]
                    cubes[s] = cubes[i]
                    cubes[i] = temp
                    return pileSort(cubes)
                s += 1
            s = 0
            while s < len(cubes):
                if cubes[i][1] == cubes[s][1]:
                    if cubes[s][0] != cubes[i][0]:
                        temp = cubes[s]
                        cubes[s] = cubes[i]
                        cubes[i] = temp
                        return pileSort(cubes)
                s += 1
    for j in range(1, len(cubes)):
        if cubes[j][0] == cubes[j - 1][0]:
            s = j
            while s < len(cubes):
                if cubes[j][0] != cubes[s][0] and cubes[j][1] == cubes[s][1]:
                    temp = cubes[s]
                    cubes[s] = cubes[j]
                    cubes[j] = temp
                    return pileSort(cubes)
                s += 1
            s = j
            while s > 0:
                if cubes[j - 1][0] != cubes[s][0] and  cubes[j - 1][1] == cubes[s][1]:
                    temp = cubes[s]
                    cubes[s] = cubes[j - 1]
                    cubes[j - 1] = temp
                    return pileSort(cubes)
                s -= 1    
    if checkLine(cubes) == False:
        return removeDupl(cubes)
    return cubes

def removeDupl(cubes):#removes the smalled cube in case of a duplicate
    newList = []
    i = 0
    while i < len(cubes) - 1:
        if cubes[i][0] == cubes[i + 1][0]:
            newList.append(cubes[i])
            i += 2
        else:
            newList.append(cubes[i])
            i += 1
    if checkLine(cubes) == False:
        return removeDupl(newList)
    return cubes

def buildTower(cubes):#prints the height of a tower and the cubes used
    try:
        cubes = pileSort(cubes)
        total = 0
        strAns = 'maximum tower height – corresponding to '
        for cube in cubes:
            total += cube[1]
            strAns += 'cube' + str(cube[2]) + ', '
        strAns = strAns[0:-2]
        print(total, strAns)
    except TypeError:
        print('Funtion parameter must be a list with format: color, edge, cube number.')

if __name__ == '__main__':
    l=[('b', 8, 1),('b', 6, 2),('b', 6, 3), ('b', 5, 4), ('b', 5, 5), ('w', 5, 6), ('w', 5, 7), ('b', 4, 8), ('r', 4, 9), ('b', 3, 10), ('b', 3, 11), ('b', 3, 12), ('r', 3, 13), ('r', 3, 14), ('r', 3, 15), ('r', 3, 16)]
    buildTower(l)
