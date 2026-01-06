#LeetCode Problem 680 Valid Palindrome II

class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        l,r=0,len(s)-1
        while l < r :
            if s[l] != s[r]:
                t=s[:l]+s[l+1:]
                if t == t[::-1]:
                    return True
                t=s[:r]+s[r+1:]
                if t == t[::-1]:
                    return True
                return False
            l+=1
            r-=1
        return False

