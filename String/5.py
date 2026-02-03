#LeetCode 2696. Minimum String Length After Removing Substrings


class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s=s.replace("AB","")
            s=s.replace("CD","")
        return len(s)