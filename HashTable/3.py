#LeetCode Problem 1207  Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=set()
        for i in d:
            if d[i] not in count:
                count.add(d[i])
            else:
                return False
        return True