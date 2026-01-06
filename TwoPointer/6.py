#LeetCode Problem 2824

class Solution(object):
    def countPairs(self, nums, target):
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]+nums[j]<target:
                    c+=1
        return c
