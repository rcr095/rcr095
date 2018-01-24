import unittest

def factorial(n): #Return the factorial n    
    nfactorial = int()    
    if n > 1:
        while n > 1:
            if nfactorial > 0:
                nfactorial = nfactorial * (n-1)
            else:
                nfactorial = n * (n-1)
            n -= 1         
    else:
        nfactorial = 1
    return nfactorial

def divide(m, n): #check if m divides n!
    try:
        factorialN = factorial(n)
        if factorialN % m == 0:
            print(str(m) + ' divides ' + str(n) + '!')
            return True
        print(str(m) + ' does not divide ' + str(n) + '!')
        return False
    except TypeError:
        print('One of the values in not an int')
        return False

class divideTests(unittest.TestCase):#unit test
    def testA(self):
        self.assertTrue(divide(9,6))
    def testB(self):
        self.assertFalse(divide(27,6))
    def testC(self):
        self.assertTrue(divide(10000,20))        
    def testD(self):
        self.assertFalse(divide(100000,20))
      
def main():
    unittest.main()

if __name__ == '__main__':
    main()
