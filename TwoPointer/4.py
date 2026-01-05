#Leet Code Problem 151  Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        cha=s.split()
        rev=cha[::-1]
        res=' '.join(ch for ch in rev)
        return res