#Problem 1 and 2 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def length(self):
        t=self
        c=0
        while t:
            c+=1
            t=t.next
        print("Length of the Linked list:",c)
    def sum(self):
        t=self
        s=0
        while t:
            s+=t.data
            t=t.next
        print("Sum of the Linked list:",s)
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
n1.length()
n1.sum()