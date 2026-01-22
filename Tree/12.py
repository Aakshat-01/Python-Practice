#LeetCode Problem 117  Populating Next Right Pointers in Each Node II

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        cl=[root]
        res=[root.val]
        while cl:
            nl=[]
            for i in range(len(cl)):
                cl[i].next=None
                if cl[i] and cl[i].left:
                    nl.append(cl[i].left)
                if cl[i] and cl[i].right:
                    nl.append(cl[i].right)
                if i<len(cl)-1:
                    cl[i].next=cl[i+1]
            cl=nl
        return root