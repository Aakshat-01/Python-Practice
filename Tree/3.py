#LeetCode Problem 145   Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def i(root,res):
            if root:
                i(root.left,res)
                i(root.right,res)
                res.append(root.val)
            return res
        return i(root,[])