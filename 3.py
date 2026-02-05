arr=[1,1,2,1,1]
ki=3
res=[]
cnt=0
# output=2
for i in range(len(arr)):
    win=[]
    for j in range(i,len(arr)):
        win=arr[i:j+1]
        if len(win)<ki:
            continue
        else:
            c=0
            for k in win:
                if k%2!=0:
                    c+=1
            if c==ki:
                res.append(win)
print(len(res))  