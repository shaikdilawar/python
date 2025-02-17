class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.Head = None

    """  def InsertAtEnd(self,data): if head and tail are used 
        newnode = Node(data)
        if self.head==None and self.tail == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode"""


    def InsertAtEnd(self,data):
        newnode = Node(data)
        if self.Head == None:
            self.Head = newnode
        else:
            temp = self.Head
            while temp.next!= None:
                temp = temp.next
            temp.next = newnode

    def InsertAtBegin(self,data):
        newnode = Node(data)
        if self.Head == None:
            self.Head = newnode
        else:
            newnode.next = self.Head
            self.Head = newnode

    def InsertAtPosition(self,pos,data):
        newnode = Node(data)
        temp=self.Head
        while(pos-1!=0):
            temp=temp.next
            pos = pos -1

        newnode.next = temp.next
        temp.next = newnode

    def DeleteAtEnd(self):
        if self.Head == None:
            print("List is Empty")
        elif self.Head.next == None:
            self.Head = None
        else:
            temp = self.Head
            while(temp.next.next != None):
                temp = temp.next 
            
            temp.next = None

    def DeleteAtBegin(self):
        if self.Head == None:
            print("List is Empty")
        elif self.Head.next == None:
            self.Head = None
        else:
            self.Head = self.Head.next
            
        
    def DeleteAtPosition(self, pos):
        if self.Head == None:
            print("List is Empty")
            return
        if(pos==1):
            self.Head = self.Head.next
        else:
            temp = self.Head
            while(pos-2):
                temp = temp.next
                pos = pos -1
                
            temp.next = temp.next.next


    def Display(self):
        temp = self.Head
        while(temp!=None):
            print(temp.data,end='->')
            temp = temp.next
            

sll = SinglyLinkedList()
sll.InsertAtEnd(2)
sll.InsertAtEnd(3)
sll.InsertAtEnd(4)
sll.InsertAtBegin(1)
sll.Display()
sll.InsertAtPosition(2,5);print()
sll.Display()
'''sll.DeleteAtEnd(); print()
sll.Display()
sll.DeleteAtBegin();print()
sll.Display()'''
sll.DeleteAtPosition(2);print()
sll.Display()
