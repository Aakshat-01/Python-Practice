#LeetCode Problem 94  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def i(root,res):
            if root:
                i(root.left,res)
                res.append(root.val)
                i(root.right,res)
            return res
        return i(root,[])