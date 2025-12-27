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
    def DBV(self,val):
        nn=Node(d)
        if self.head==None:
            self.head=nn
            self.tail=nn
        else:
            t=self.head
            while t.next.data != val:
                t=t.next
            t.next=t.next.next
        
s1=SLL()
while True:
    op=int(input("1.IAS  2.IAE  3.IBP  4.DAS  5.DAE  6.DBP  7.DBV  :--"))
    if op==1:
        d=input("Enter data for IAS:")
        s1.IAS(d)
    elif op==2:
        d=input("Enter data for IAE:")
        s1.IAE(d)
    elif op==3:
        d=input("Enter data for IAB:")
        p=int(input("Enter position for data to be inserted :"))
        s1.IBP(d,p)
    elif op==4:
        s1.DAS()
    elif op==5:
        s1.DAE()
    elif op==6:
        p=int(input("Enter data position to be deleted after:"))
        s1.DBP(p)
    elif op==8:
        s1.display()
    elif op==7:
        val=input("Enter data value to be deleted:")
        s1.DBV(val)
    else:
        print("Invalid Option")
