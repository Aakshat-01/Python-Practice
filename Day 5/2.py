#Problem 1
arr=[5,4,5,1,6,7]
s=arr[0]
for i in arr:
    if s>i:
        s=i
print(s)

#Problem 2
arr=['abc', 'xyz', 'aba', '1221']
c=0
for i in arr:
    if(i[0]==i[-1]):
        c+=1

print(c)

#Problem 3
arr=[4,3,6,1,7,2,1,6,9]
l=set(arr)
print(l)