arr= [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
arr1=[]
for i in arr:
    if type(i) == list:
        l=len(i)
        for j in range(l):
            arr1.append(i[j])
    else:
        arr1.append(i)
print(arr1)