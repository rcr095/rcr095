'''
Create a tree to store information and implement the following operations:
• Find a student by his/hers unique code, and support updating of the student info if found.
• List students by class in lexicographic order of their names.
• List all students in lexicographic order of their names.
• List all graduated students.
• List all undergrads by their class in lexicographic order of their names.
• Delete a student given by its code.
• Delete all graduates.
'''
class Student:
    def __init__(self, uniqueCode, name, birthDate, address, classID, enrolmentDate, status):
        self.uniqueCode = uniqueCode
        self.name = name
        self.birthDate = birthDate
        self.address = address
        self.classID = classID
        self.enrolmentDate = enrolmentDate
        self.status = status
        self.self = self
        self.all = self.uniqueCode, self.name, self.birthDate, self.address, self.classID, self.enrolmentDate, self.status

    def update(self):#updates self.all
        self.all = self.uniqueCode, self.name, self.birthDate, self.address, self.classID, self.enrolmentDate, self.status
        
    def display(self):#displays self.all
        print(self.all)

class BinTreeNode:
    '''
    Title: Binary Tree Search in Python
    Author: Hintea, D.
    Date: 2017
    Availability: http://moodle.coventry.ac.uk
    '''
    def __init__(self, memAdr):
        self.self = memAdr
        self.left = None
        self.right = None

def tree_insert(tree, student):#insert new student to tree
    '''
    Title: Binary Tree Search in Python
    Author: Hintea, D.
    Date: 2017
    Availability: http://moodle.coventry.ac.uk
    '''
    if tree == None:
        tree = BinTreeNode(student)
    else:
        if(student.name < tree.self.name):
            if tree.left == None:
                tree.left = BinTreeNode(student)
            else:
                tree_insert(tree.left,student)
        else:
            if tree.right == None:
                tree.right = BinTreeNode(student)
            else:
                tree_insert(tree.right,student)
    return tree

def find(tree, uniqueCode):#finds a student by its uniquecode
    if tree.self.uniqueCode == uniqueCode:
        return tree.self.self
    if tree.left != None:
        if find(tree.left, uniqueCode) != None:
            return find(tree.left, uniqueCode)
    if tree.right != None:
        if find(tree.right, uniqueCode) != None:
            return find(tree.right, uniqueCode)

def update(tree, uniqueCode, info2Upd):#updates the information of a student with a given uniquecode
    student = find(tree, uniqueCode)
    info2Upd = info2Upd.lower()
    if student != None:
        if info2Upd == 'name':
            student.name = input('Current Info: ' + str(student.name) + '\nNew Info: ')
            student.update()
        elif info2Upd == 'birthdate':
            student.birthDate = input('Current Info: ' + str(student.birthDate) + '\nNew Info: ')
            student.update()
        elif info2Upd == 'address':
            student.address = input('Current Info: ' + str(student.address) + '\nNew Info: ')
            student.update()
        elif info2Upd == 'classid':
            student.classID = input('Current Info: ' + str(student.classID) + '\nNew Info: ')
            student.update()
        elif info2Upd == 'enrolmentdate':
            student.enrolmentDate = input('Current Info: ' + str(student.enrolmentDate) + '\nNew Info: ')
            student.update()
        elif info2Upd == 'status':
            student.status = input('Current Info: ' + str(student.status) + '\nNew Info: ')
            student.update()
        else:
            print('No Info')
    else:
        print('No student')
        
###FUNTIONS WITH CLASS CODITION###
def findAll(tree):#returns every unique class
    ret = []
    if tree.left != None:
        ret += findAll(tree.left)
    if tree.right != None:
        ret += findAll(tree.right)    
    ret += [tree.self.classID]
    newRet = []
    for i in ret:
        if i not in newRet:
            newRet.append(i)
    return newRet

def sort(listA):
    if len(listA) <= 0:
        return listA
    pivot = listA[-1]
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
    return sort(smallList)+mid+sort(bigList)

def inOrder(tree, byClass):#return the student names in order
    if byClass.lower() == 'yes':#return the student names in order BY CLASS
        classes = findAll(t)
        classes = sort(classes)
        for clasS in classes:
            print(clasS,':')
            classSrch(tree, clasS)
            print('\n')
    else:
        classSrch(tree, None)
        
def classSrch(tree, classID):#list students in lexicographic order by their names and class
    if classID == None:
        if tree.left != None:
            classSrch(tree.left, classID)
        print (tree.self.name)
        if tree.right != None:
            classSrch(tree.right, classID)
    else:
        if tree.left != None:
            classSrch(tree.left, classID)
        if tree.self.classID == classID:
            print (tree.self.name)
        if tree.right != None:
            classSrch(tree.right, classID) 

###FUNTION WITH STATUS CONDITION###       
def statusSrch(tree, status):#list students in lexicographic order by their names and status
        if tree.left != None:
            statusSrch(tree.left, status)
        if tree.self.status == status:
            print (tree.self.name)
        if tree.right != None:
            statusSrch(tree.right, status)

def statusClassSrch(tree, classID, status):
        if tree.left != None:
            statusClassSrch(tree.left, classID, status)
        if tree.self.status == status and tree.self.classID == classID:
            print (tree.self.name)
        if tree.right != None:
            statusClassSrch(tree.right, classID, status)

def statusClassRun(tree, status):
    classes = findAll(tree)
    for classID in classes:
        print(classID + ':')
        statusClassSrch(tree, classID, status)
            
###DELETE FUNCTIONS###
def deleteStudent(tree, uniqueCode):#deletes the student with the given uniqueCode
    if find(tree, uniqueCode) == None:
        print('No Student')
        return False
    student = find(tree, uniqueCode)
    if tree == None:
        return tree 
    elif student.name < tree.self.name:
        tree.left = deleteStudent(tree.left, uniqueCode)
    elif student.name > tree.self.name:
        tree.right = deleteStudent(tree.right, uniqueCode)
    else:
        if tree.left == None and tree.right == None:
            tree = None
            return tree        
        elif tree.left == None :
            temp = tree.right 
            tree = None
            return temp   
        elif tree.right == None :
            temp = tree.left 
            tree = None
            return temp
        else:
            temp = findMin(tree.right)
            tree.self = temp.self
            tree.right = deleteStudent(tree.right , temp.self.uniqueCode)
    return tree

def findMin(tree):#finds smallest ellement on a tree
    while(tree.left != None):
        tree = tree.left 
    return tree

def findGrad(tree):#finds all graduates
    ret = []
    if tree.self.status.lower() == 'graduate':
        ret += [tree.self.uniqueCode]       
    if tree.left!=None:
        ret += findGrad(tree.left)        
    if tree.right!=None:
        ret += findGrad(tree.right)        
    return ret

def deleteGrad(tree):#deletes all draduates
    grads = findGrad(tree)
    for student in grads:
        deleteStudent(tree, student)

if __name__ == '__main__':
    t=tree_insert(None, Student(1234, 'john', '01/02/90', 'some street', 'c123', '20/09/2016', 'graduate'));
    tree_insert(t, Student(1222, 'jihn', '01/02/90', 'some street', 'c121', '20/09/2016', 'undergrad'))
    tree_insert(t, Student(1226, 'juhn', '01/02/90', 'some street', 'c122', '20/09/2016', 'undergrad'))
    tree_insert(t, Student(1255, 'jahn', '01/02/90', 'some street', 'c123', '20/09/2016', 'undergrad'))
    tree_insert(t, Student(1211, 'jehn', '01/02/90', 'some street', 'c122', '20/09/2016', 'graduate'))
    print('Student 1222:')
    findStudent = find(t, 1222)
    print(findStudent.name, '\n')
    print('Students by class:')
    inOrder(t, 'yes')
    print('Students:')
    inOrder(t, 'no')
    print('\n' + 'Graduates:')
    statusSrch(t, 'graduate')
    print('\n' + 'Undergrad by Class:')
    statusClassRun(t, 'undergrad')
    print('\nBefore Deleting:')
    inOrder(t, 'no')
    deleteStudent(t, 1222)
    print('\nAfter Deleting:')
    inOrder(t, 'no')
    print('\nBefore Deleting Graduates:')
    statusSrch(t, 'graduate')
    deleteGrad(t)
    print('\nAfter Deleting Graduates:')
    statusSrch(t, 'graduate')
