#LeetCode Problem 104  Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cl=[root]
        res=[[root.val]]
        while cl:
            nl=[]
            for n in cl:
                if n and n.left:
                    nl.append(n.left)
                if n and n.right:
                    nl.append(n.right)
            cl=nl
            if cl:
                res.append([n.val for n in cl])
        return len(res)