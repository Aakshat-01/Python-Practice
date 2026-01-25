#LeetCode Problem 875.  Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            mid=(l+r)//2
            hr=0
            for p in piles:
                hr+=math.ceil(p/mid)
            if hr<=h:
                r=mid-1
            else:
                l=mid+1
        return l
