#LeetCode Problem 98  Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def i(r,res):
            if r:
                i(r.left,res)
                res.append(r.val)
                i(r.right,res)
            return res
        res=i(root,[])
        return len(res)==len(set(res)) and res==sorted(res)
