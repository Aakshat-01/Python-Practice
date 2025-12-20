#Problem 1
arr=[2,3,7,13,17]
for i in arr:
    c=0
    for j in range(1,i):
        if i%j ==0 :
            c+=1
    if c>=2:
        print(False)
        exit()
print(True)

