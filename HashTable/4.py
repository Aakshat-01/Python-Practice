#LeetCode Problem 205  Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # if len(set(s)) == len(set(t)):
        #     return True
        # else:
        #     return False
        d_s_t={}
        d_t_s={}
        li=[]
        for i in range(len(s)):
            d_s_t[s[i]]=t[i]
            d_t_s[t[i]]=s[i]
        print(d_s_t)
        print(d_t_s)
        # for i in range(len(s)):
        #     li.append(d_s_t[s[i]])
        # print(li)
        # if "".join(li) == t:
        #     return True
        # else:
        #     return False
        