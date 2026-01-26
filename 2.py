s="aa"
k=1
# s="abc"
# k=2
# output- 3
res=[]
if len(set(s))==k:
    print(len(s))
else:
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            win=s[i:j]
            print(win)
            if len(set(win))<=k:
                if len(res)<len(win):
                    res=win
    print(len(res))