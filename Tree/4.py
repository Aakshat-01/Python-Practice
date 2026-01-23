#LeetCode 102  Binary Tree Level Order Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return res