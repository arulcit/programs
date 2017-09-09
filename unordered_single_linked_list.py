class Node:
    def __init__(self,data=None,nt=None):
        self.data = data
        self.nt = nt

    def setdata(self,data):
        self.data = data

    def setnext(self,nt1):
        self.nt = nt1

    def getdatanext(self):
        return self.nt.data

    def getnodenext(self):
        return self.nt

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        temp = Node(data)
        if self.head != None:
            temp.nt = self.head
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.nt
        print "Size: %d" % count
    def printall(self):
        current = self.head
        while current:
            print current.data,
            current = current.nt
        print

    def search(self,data):
        current = self.head
        bo = False
        while current and not bo:
            if current.data == data:
                print "Found %d" % current.data
                bo = True
                return current
            else:
                current = current.nt
        if bo == False:
            print "Not Found %d" % data
            return None

    def remove(self,val):
        current = self.head
        prev = None
        boo = False
        while current and not boo:
            if current.data == val:
                if prev == None:
                    self.head = current.getnodenext()
                    boo = True
                else:
                    prev.nt = current.getnodenext()
                    boo = True
            prev = current
            current = current.getnodenext()



a = LinkedList()

a.add(5)
a.printall()
a.add(10)
a.printall()
a.add(15)
a.printall()
a.add(20)
a.printall()
a.size()
b = a.search(10)
print "Data Searched",b.data
print "-" * 20
a.remove(15)
b = a.search(15)
if b:
    print "Data Searched",b.data
a.printall()
print "-" * 20
a.remove(5)
b = a.search(35)
if b:
    print "Data Searched",b.data
a.size()
a.printall()
print "-" * 20
a.remove(10)
a.printall()
a.size()
print "-" * 20
a.remove(200)
b = a.search(20)
if b:
    print "Data Searched",b.data
a.printall()
a.size()

