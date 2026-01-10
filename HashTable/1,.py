#LeetCode Problem 409 Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        odd = 0
        for i in count:
            if count[i]%2 != 0:
                odd += 1
        return len(s) - odd + 1
    