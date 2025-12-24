class Solution(object):
    def isAnagram(self, s, t):
        v={}
        u={}
        for i in s:
            if i in v:
                v[i]+=1
            else:
                v[i]=1
        for i in t:
            if i in u:
                u[i]+=1
            else:
                u[i]=1
        if u == v:
            return True
        else:
            return False
