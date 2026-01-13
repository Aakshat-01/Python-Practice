#LeetCode Problem 205  Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d_s_t={}
        d_t_s={}
        li=[]
        for i in range(len(s)):
            d_s_t[s[i]]=t[i]
            d_t_s[t[i]]=s[i]
        
        if list(d_s_t.keys()) == list(d_t_s.values()):
            return True
        else:
            return False