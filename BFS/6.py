#LeetCode Problem 230. Kth Smallest Element in a BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def i(root,res):
            if root:
                i(root.left,res)
                res.append(root.val)
                i(root.right,res)
            return res
        res=i(root,[])
        print(res)
        return res[k-1]