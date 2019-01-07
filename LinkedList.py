class Node():
    def __init__(self,n):
        self.data = n
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add(self,n):
        if(self.head==None):
            temp = Node(n)
            self.head = temp
            print("in None loop")
        else:
            # add to start - push
            temp = Node(n)
            temp.next = self.head
            self.head = temp
            print("in ELSE loop")
            #Add to end - Queue
            

    def popLL(self):
        if(self.head==None):
            print("Nothing to delete")
        else:
            #if(self.head.next!=None):
            temp =  self.head.next
            self.head = temp

    #def deQueueQ(self):

    def deleteAll(self,n):
        helper = Node(None)
        helper.next = self.head
        temp = helper
        if(self.head==None):
            print("No data to delete")
        else:
            while(temp.next!=None):
                if(temp.next.data == n):
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        self.head = helper.next

    def printLL(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end=",")
            temp = temp.next
    
if __name__ =='__main__':
    ll = LinkedList()
    ll.add(2)
    ll.add(3)
    ll.add(2)
    ll.add(1)
    ll.add(2)
    ll.add(2)
    ll.add(5)
    ll.add(2)
    ll.add(2)
    ll.add(2)
    ll.printLL()
    ll.deleteAll(2)
    print()
    ll.printLL()
    
