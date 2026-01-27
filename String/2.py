#LeetCode Problem 58  Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        return len(l[-1])