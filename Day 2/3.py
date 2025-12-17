l1=int(input("Enter length of side 1 of the triangle:"))
l2=int(input("Enter length of side 2 of the triangle:"))
l3=int(input("Enter length of side 3 of the triangle:"))

if(l1 != l2 and l1 != l3 and l2 != l3):
    print("Scalene triangle")
elif(l1 == l2 and l1 == l3 and l2 == l3):
    print("Equilateral triangle")
else:
    print("Isosceles triangle")
