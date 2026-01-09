#LeetCode Problem 2461  Maximum Sum of Distinct Subarray With Length K

class Solution:
    def maximumSum(self, nums: List[int], k: int) -> int:
        return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))

#Time Complexity : O(N)
#Space Complexity : O(1)
