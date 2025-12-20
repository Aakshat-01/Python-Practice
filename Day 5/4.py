arr=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,4]
unique=set(arr)
for i in unique:
    c=0
    for j in arr:
        if(i==j):
            c+=1
    print("Frequency of",i,":",c)