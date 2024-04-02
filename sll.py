class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList(self):
    def __init__(self):
        self.head=None
    def insertFront(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def insertEnd(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current:
            current=current.next
        current.next=new_node
    def deleteFront(self):
        if not self.head:
            print('EMPTY')
            return
        self.head=self.head.next
    def deleteEnd(self):
        if not self.head:
            print('EMPTY')
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=None
