#Problem 5 and 6
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def search(self,element):
        t=self
        while t:
            if t.data==element:
                print("Element Found")
                break
            t=t.next
        else:
            print("Element not in Linked List")
    def count(self, element):
        t=self
        m=t.data
        c=0
        while t:
            if t.data==element:
                c+=1
            t=t.next
        print("Occurences of Element in Linked list:",c)
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(40)
n6=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n1.search(50)
n1.count(40)
