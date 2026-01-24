#LeetCode Problem 1302  Deepest Leaves Sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
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
        return sum(res[-1])