from fractions import Fraction
n=int(input("Input number of terms:"))
s=0
for i in range(1, n+1):
    print(Fraction(1,i), end=" + ")
    # print("1/",i, end=" + ")
    s=s+(1/i)
print("\n",s)