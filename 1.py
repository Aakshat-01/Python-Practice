# arr=[1,1,0,0,1,1,1]
arr=[1,1,1,1,1,1,1,0]
k=1
#Output - 4
res=[]
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        win=arr[i:j]
        if win.count(0)<=k:
            if len(res)<len(win):
                res=win
print(len(res)+1)