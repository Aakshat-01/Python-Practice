#LeetCode Problem 2461  Maximum Sum of Distinct Subarrays With Length K


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        begin = 0
        end = 0
        d = {}
        while end < len(nums):
            curr_num = nums[end]
            last = d.get(curr_num, -1)
            while begin <= last or end - begin + 1 > k:
                current_sum -= nums[begin]
                begin += 1
            d[curr_num] = end
            current_sum += nums[end]
            if end - begin + 1 == k:
                ans = max(ans, current_sum)
            end += 1
        return ans