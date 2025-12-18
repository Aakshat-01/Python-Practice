n=int(input("Input number of terms:"))
num='9'
s=0
for i in range(1,n+1):
    print(num, end=" ")
    num=num+'9'
    s=s+int(num)
print("\n",s)