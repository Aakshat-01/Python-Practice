class Solution(object):
    def containsDuplicate(self, nums):
        v={}
        for n in nums:
            if n in v:
                return True
            else:
                v[n]=1
        return False