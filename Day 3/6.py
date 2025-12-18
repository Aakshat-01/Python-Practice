n=int(input("Enter the number:"))
s=0
for i in range(1,n):
    if(n%i==0):
        print(i, end=" ")
        s+=i
print("\nThe sum of divisor is:",s)
if(n==s):
    print("It is a perfect number")
else:
    print("It is not a perfect number")