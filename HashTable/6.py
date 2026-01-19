#LeetCode Problem 496  Next Greater Element I


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        d={}
        for i in nums1:
            p=nums2.index(i)
            for j in nums2[p:]:
                if j>i:
                    res.append(j)
                    break
            else:
                res.append(-1)
        return res
