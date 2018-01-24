import numpy as np

def checkMove(row, column, solution):#validates a position for a new queen
    for queen in solution:
        ir, ic = queen
        if row == ir:#check row
            return False
        if column == ic:#check column
            return False
        i = row
        j = column
        while i > 0:#chek diagonal left
            if i - 1 == ir and j - 1 == ic:
                return False
            i -= 1
            j -= 1
        i = row
        j = column
        while i > 0:#chek diagonal right
            if i - 1 == ir and j + 1 == ic:
                return False
            i -= 1
            j += 1
    return True

def solutions(n):#creates a list of possible solutions and fills it from the 'top'
    solutions = []
    for row in range(n):
        solutions = getSolution(solutions, row, n)
    return solutions

def getSolution(solutions, row, n):#adds a new queen to the list
    newSolutions = []
    for column in range(n):
        if len(solutions) == 0:
            newSolutions.append([] + [(row,column)])
        else:
            for solution in solutions:
                if checkMove(row, column, solution) == True:
                    newSolutions.append(solution + [(row, column)])  
    return newSolutions

def createMatrix(n):
    matrix = np.arange(n*n).reshape(n, n) 
    for i in matrix: 
        for j in range(len(i)):
            i[j] = 0
    return matrix

def matrixSolution(n):#displays the solutions as matrices
    solutionList = solutions(n)
    boards = []
    for solution in solutionList:
        board = createMatrix(n)
        for queen in solution:
            r, c = queen
            board[r, c] = 1
        print(board, '\n')

def listSolution(n):#displays the solutions
    solutionList = solutions(n)
    for solution in solutionList:
        print(solution)
        
if __name__ == '__main__':
    matrixSolution(4)
    listSolution(4)
