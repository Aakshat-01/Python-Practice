class Solution(object):
    def reverseString(self, s):
        l=len(s)
        start=0
        last=l-1
        while(start<last):
            s[start],s[last]=s[last],s[start]
            start+=1
            last-=1
        