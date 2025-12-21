class Solution(object):
    def reverseVowels(self, s):
        vowels=set('aeiouAEIOU')
        s=list(s)
        l=len(s)
        st=0
        ls=l-1
        while(st<ls):
            if s[st] not in vowels:
                st+=1
            elif s[ls] not in vowels:
                ls-=1
            else:
                s[st],s[ls]=s[ls],s[st]
                st+=1
                ls-=1
        return "".join(s)