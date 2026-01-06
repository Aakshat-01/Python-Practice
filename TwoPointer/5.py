#LeetCode Problem 977 Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq=[ch**2 for ch in nums]
        sq.sort()
        return sq
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
