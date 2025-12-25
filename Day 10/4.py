#Problem 7
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def avg(self):
        t=self
        s=0
        c=0
        while t:
            c+=1
            s+=t.data
            t=t.next
        avg=s/c
        print("Average of the Linked list:",avg)
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
n1.avg()
