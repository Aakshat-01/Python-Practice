#LeetCode Problem 290  Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st=s.split(" ")
        if len(pattern) != len(st) or len(set(pattern)) != len(set(st)):
            return False
        h={}
        for i in range(len(pattern)):
            if pattern[i] in h:
                if h[pattern[i]]!=st[i]:
                    return False
            else:
                h[pattern[i]]=st[i] 
        return True
