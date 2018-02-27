'''
Convert A into B as cheaply as possible. The rules are as follows:
• For a cost of 3 you can delete any letter.
• For a cost of 4 you can insert a letter in any position.
• For a cost of 5 you can replace any letter by any other letter.
'''

import unittest

def check(a, b):#check if string equality
    for l in range(len(a)):
        if a[l] != b[l]:
            return False
    return True
    
def convert(a, b, cost = 0):
    if check(a, b) == False:
        lenA = len(a)
        lenB = len(b)
        temp = str()
        if lenA == lenB:
            l = 0
            while l < lenA:
                if a[l] == b[l]:
                    temp += a[l]
                    l += 1
                #delete a letter if the next 'A' letter is equal to current 'B' and different from next 'B'
                elif l+1 < lenA and a[l + 1] != b[l + 1] and a[l + 1] == b[l]:
                    temp += a[l + 1:lenA]
                    l += 1
                    cost += 3
                    return convert(temp, b, cost)
                #convert a letter
                else:
                    temp += b[l] + a[l + 1:lenA]
                    cost += 5
                    return convert(temp, b, cost)    
            return a, cost
        elif lenA > lenB:#delete the first non equal letter in case string 'A' is longer than 'B'
            for l in range(lenB):
                if a[l] != b[l]:
                    temp += a[l + 1:lenA]
                    cost += 3
                    return convert(temp, b, cost)
                temp += a[l] 
        elif lenA < lenB:
            l = 0
            while l < lenA:
                if a[l] == b[l]:
                    temp += a[l]
                    l += 1
                else:#add a letter to the first space that differs from 'B'
                    temp += b[l] + a[l:lenA]
                    cost += 4
                    return convert(temp, b, cost)
            temp += b[l]
            cost += 4
            return convert(temp, b, cost)       
    return a, cost

class conversionTest(unittest.TestCase):
    def testA(self):
        self.assertEqual(convert('abcabc', 'abaabc'), ('abaabc', 5))
    def testB(self):
        self.assertEqual(convert('abcabc', 'abacab'), ('abacab', 17))
    def testC(self):
        self.assertEqual(convert('abcabac', 'abcabc'), ('abcabc', 3))
    def testD(self):
        self.assertEqual(convert('abc', 'ababc'), ('ababc', 8))
    def testE(self):
        self.assertEqual(convert('acbacb', 'abaaab'), ('abaaab', 12))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
                
