#Problem 3 and 4
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def maxi(self):
        t=self
        m=t.data
        while t:
            if t.data>m:
                m=t.data
            t=t.next
        print("Maximum Element in Linked list:",m)
    def mini(self):
        t=self
        m=t.data
        while t:
            if t.data<m:
                m=t.data
            t=t.next
        print("Minimum Element in Linked list:",m)
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
n1.maxi()
n1.mini()
