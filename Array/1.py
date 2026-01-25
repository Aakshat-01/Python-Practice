#LeetCode Problem 905 Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums)==1:
            return nums 
        odd=[]
        even=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.extend(odd)
        return even