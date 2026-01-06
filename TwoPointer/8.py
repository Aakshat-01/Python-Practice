#LeetCode Problem 1423 Maximum Points You Can Obtain from Cards

class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        if k == n:
            return sum(cardPoints)
        s=sum(cardPoints[:k])
        ms=s
        for i in range(k-1,-1,-1):
            s= s-cardPoints[i]+cardPoints[-k+i]
            ms=max(s,ms)
        return ms
