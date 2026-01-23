#LeetCode Problem 637 Average of Levels in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        cl=[root]
        res=[[root.val]]
        avg=[]
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
            avg.append(sum(i)/len(i))
        return avg
