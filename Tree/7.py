#LeetCode Problem 515  Find Largest Value in Each Tree Row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cl=[root]
        lar=[]
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
        for i in res:
            lar.append(max(i))
        return lar