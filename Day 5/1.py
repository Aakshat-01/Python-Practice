#Problem 1 
arr=[1,2,3,4,5,6,7]
s=sum(arr)
print(s)

#Problem 2
arr=[1,2,3,4,5,6,7]
mul=1
for i in arr:
    mul*=i
print(mul)

#Problem 3
arr=[1,2,3,35,4,5,6,7]
l=arr[0]
for i in arr:
    if l<i:
        l=i
print(l)