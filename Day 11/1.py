class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def IAS(self,d):
        nn=Node(d)
        if self.head==None:
            self.head=nn
            self.tail=nn
        else:
            nn.next=self.head
            self.head=nn

    def IAE(self,d):
        nn=Node(d)
        if self.head==None:
            self.head=nn
            self.tail=nn
        else:
            self.tail.next=nn
            self.tail=nn

    def DAS(self):
        if self.head==None:
            print("SLL is empty")
        else:
            self.head=self.head.next

    def DAE(self):
        if self.head==None:
            print("SLL is empty")
        else:
            t=self.head
            while t.next!=self.tail:
                t=t.next
            self.tail=t
            t.next=None

    def display(self):
        t=self.head
        while t:
            print(t.data, end="->")
            t=t.next
        print()
    def IBP(self,d,p):
        nn=Node(d)
        if self.head==None:
            self.head=nn
            self.tail=nn
        else:
            t=self.head
            c=1
            while c<p-1:
                t=t.next
                c+=1
            curr=t.next
            t.next=nn
            nn.next=curr

    def DBP(self,p):
        if self.head==None:
            print("SLL is empty")
        else:
            t=self.head
            c=1
            while c<p-1:
                t=t.next
                c+=1
            t.next=t.next.next
            self.tail=t
