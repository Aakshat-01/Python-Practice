n=int(input("Enter number of terms:"))
n1=0
n2=1
n3=0
for i in range(1,n+1):
    print(n1, end=" ")
    n3=n1+n2
    n1=n2
    n2=n3