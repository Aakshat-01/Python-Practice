#LeetCode Problem 387  First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in s:
            if d[i]==1:
                return s.index(i)
        else:
            return -1
            