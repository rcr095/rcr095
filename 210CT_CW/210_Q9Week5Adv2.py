import string

class Node(object):
    '''
    Title: Doubly Linked List Implementation
    Author: Hintea, D.
    Date: 2017
    Availability: http://moodle.coventry.ac.uk
    '''
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Linked(object):
    '''
    Funtions init and insert(up to prepend node comment)
    Title: Doubly Linked List Implementation
    Author: Hintea, D.
    Date: 2017
    Availability: http://moodle.coventry.ac.uk
    '''
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, prevN, node):
        if prevN != None:
            node.next = prevN.next
            prevN.next = node
            node.prev = prevN
            if node.next != None:
                node.next.prev = node
        if self.head == None:
            self.head = self.tail = node
            node.prev = node.next=None
        #Prepends node
        elif prevN == None:
            self.head.prev = node
            node.next = self.head
            self.head = node
        elif self.tail == prevN:
            self.tail = node
    def displayF(self):#prints list from head to tail
        dataList = []
        h = self.head
        while h != None:
            dataList.append(h.data)
            h = h.next
        print(dataList)
    def displayL(self):#prints list from tail to head
        dataList = []
        t = self.tail
        while t != None:
            dataList.append(t.data)
            t = t.prev
        print(dataList)
            
def lenSort(list):#returns a list of string sorted by the length of its elements
    if len(list) <= 1:
        return list
    pivot = list[0]
    bigList = []
    mid = []
    smallList = []
    for i in list:
        if i == pivot:
            mid.append(i)
        elif len(i) < len(pivot):
            smallList.append(i)
        else:
            bigList.append(i)
    return (lenSort(smallList) + mid + lenSort(bigList))  

def stringSort(list):#returns a list of strings alphabetically sorted 
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
    return (stringSort(smallList) + mid + stringSort(bigList))

def linkedSort(file):
    text = open(file, 'r')
    l = []
    for line in text: #appends the words in a file to a list removing duplicates
        for word in line.split():
            word = word.strip(string.punctuation)
            if word not in l:
                l.append(word.lower())
    l = lenSort(l)
    lists = []
    curList = []
    curLen = 0
    for i in range(len(l)):#creates double linked lists with a list of words, different lists for different word lengths
        a = l[i]
        if len(a) == curLen:
            curList[0].insert(curList[0].tail, Node(a))
        else:
            curList = [['string%s' % i]]
            curList[0] = Linked()
            curList[0].insert(None, Node(a))
            lists.append(curList[0])
            curLen = len(a)
            
    for j in lists:
        j.displayF()
        
if __name__ == '__main__':
    linkedSort('input.txt')



