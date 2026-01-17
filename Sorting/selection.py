#Selection Sort

a=[6,3,4,5,2,3,1,9,2]
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[j]<a[i]:
            a[j],a[i]=a[i],a[j]
print(a)
