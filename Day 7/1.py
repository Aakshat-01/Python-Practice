class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1.extend(nums2)
        for i in range(m+n):
            if 0 in nums1 and len(nums1)>m+n:
                nums1.remove(0)
        nums1.sort()
      