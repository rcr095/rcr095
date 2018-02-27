'''
A lorry can carry at most n kilograms. The name of the materials, the amount of material in
kilograms and the material price per kilo are known. Compute a load composition in such a way
that the value (price) of the load is maximum.
'''
import unittest

'''
Takes a maximum load value and a list of materials,their value per kiloand ammount available.
Prints the load info, materials and their weight,aswell as the load value.
Returns load value
'''

def step(matList):#returns information for the material with the highest value
    highVal = int()
    highValName = str()
    highValWei = int()
    for material in matList:
        if material[2] > highVal:
            highVal = material[2]
                
    for material in matList:
        if material[2] == highVal:
            material[2] = 0
            highValName = material[0]
            highValWei = material[1]
            
    return highValName, highValWei, highVal

def lorry(load, matList):
    try:
        matListLen = len(matList)
        freeLoad = load
        loadValue = 0
        loadMat = []
        loadInfo = str()
        #loop runs step function until it reaches maximum load or runs out of materials
        while matListLen > 0 and freeLoad > 0:
            stepReturn = step(matList)
            if freeLoad - stepReturn[1] >= 0:
                loadMat.append([stepReturn[0], stepReturn[1]])
                loadValue = loadValue + stepReturn[1]*stepReturn[2]
                freeLoad = freeLoad - stepReturn[1]
            else:
                loadMat.append([stepReturn[0], freeLoad])
                loadValue = loadValue + freeLoad*stepReturn[2]
                freeLoad = 0
            matListLen -= 1
        #creates the load information, the materials and the weights
        loadMatLen = len(loadMat)-1
        loadInfo = str(loadMat[loadMatLen][1])+'Kg of '+str(loadMat[loadMatLen][0])
        while loadMatLen > 0:
            loadMatLen -= 1
            loadInfo = loadInfo+' and '+str(loadMat[loadMatLen][1])+'Kg of '+str(loadMat[loadMatLen][0])        
        print('\n','Load composition value =', loadValue)    
        print('\n',loadInfo)
        return loadValue, loadInfo
    except TypeError:
        print('One of the parameters is not correct.')
        return False
    
class lorryTests(unittest.TestCase):
    def testA(self):
        self.assertEqual(lorry(10, [['copper', 7, 65], ['plastic', 15, 50], ['gold', 4, 100]]), (790, '6Kg of copper and 4Kg of gold'))
    def testB(self):
        self.assertEqual(lorry(10, [['copper', 2, 65], ['plastic', 15, 50], ['gold', 4, 100]]), (730, '4Kg of plastic and 2Kg of copper and 4Kg of gold'))
    def testC(self):
        self.assertEqual(lorry(50, [['dirt', 50, 10], ['plastic', 5, 50], ['gold', 5, 100]]), (1150, '40Kg of dirt and 5Kg of plastic and 5Kg of gold'))
    def testD(self):
        self.assertEqual(lorry(100, [['dirt', 70, 10], ['plastic', 15, 50], ['gold', 10, 100]]), (2450, '70Kg of dirt and 15Kg of plastic and 10Kg of gold'))
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()







