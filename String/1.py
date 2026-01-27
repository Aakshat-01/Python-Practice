#LeetCode Problem 434  Number of Segments in a String

class Solution:
    def countSegments(self, s: str) -> int:
        l=s.split()
        return len(l)