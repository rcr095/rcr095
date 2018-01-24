import unittest

def quickSort(m, listA): #uses quicksort to return the mth element
    state = False
    pivot = listA[m-1]
    for x in range(len(listA) - 1):
        if listA[x] <= listA[x + 1]:
            state = True
        else:
            pivot = listA[x]
            state = False
            break
    bigList = []
    mid = []
    smallList = []    
    for i in listA[0: len(listA)]:
        if i == pivot:
            mid.append(pivot)        
        elif i < pivot:
            smallList.append(i)
        else:
            bigList.append(i)
    if state == True:
        return listA[m-1]    
    return quickSort(m, smallList+mid+bigList)

class sortTests(unittest.TestCase):
     def testA(self):
          self.assertEqual(quickSort(5, [9, 5, 8, 5, 4, 3, 1, 2]), 5)

def main():
     unittest.main()

if __name__ == '__main__':
     main()
