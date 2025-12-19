#Problem 1
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#Problem 2
for i in range(1,5):
    for k in range(4-i,0,-1):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#Problem 3
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()