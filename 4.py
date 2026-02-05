s="aaeeiioouu"
res=[]
if 'a' not in s or 'e' not in s or 'i' not in s or 'o' not in s or 'u' not in s:
    print('0')
else:
    for i in range(len(s)):
        for j in range(i,len(s)):
            win=s[i:j+1]
            if 'a' in win and 'e' in win and 'i' in win and 'o' in win and 'u' in win:
                res.append(win)
    # print(res)
    ans=len(res[0])
    for i in res:
        if len(i)<ans:
            ans=len(i)
    print(ans)