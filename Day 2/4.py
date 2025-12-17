x=int(input("Enter x coordinate:"))
y=int(input("Enter y coordinate:"))

if(x>0 and y>0):
    print("First Quad")
elif(x<0 and y>0):
    print("Second Quad")
elif(x<0 and y<0):
    print("Third Quad")
elif(x>0 and y<0):
    print("Fourth Quad")
elif(x==0 and y==0):
    print("Centre")
elif(x==0 and y!=0):
    print("Y Axis")
elif(x!=0 and y==0):
    print("x Axis")
