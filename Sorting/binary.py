a=[1,2,3,4,5,6,7,8,9,10]
t=8
l,r=0,len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==t:
        print("Found")
        break
    elif t<a[mid]:
        r=mid-1
    else:
        l=mid+1