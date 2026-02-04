#LeetCode Problem 389. Find the Difference


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)

        for ch in ct:
            if ct[ch] != cs[ch]:
                return ch