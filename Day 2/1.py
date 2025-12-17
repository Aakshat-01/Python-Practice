a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a>b and a>c):
    print(a,"is the greatest amongst the three numbers")
elif(b>a and b>c):
    print(b,"is the greatest amongst the three numbers")
elif(c>a and c>b):
    print(c,"is the greatest amongst the three numbers")
elif(a==b and a<c):
    print(a,"and",b,"are equal and less than",c)
elif(a==c and a<b):
    print(a,"and",c,"are equal and less than",b)
elif(b==c and b<a):
    print(b,"and",c,"are equal and less than",a)
elif(a==b and a==c):
    print("All three numbers are equal")