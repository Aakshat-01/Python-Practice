#LeetCode Problem 1249 Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        stack=[]
        for i,c in enumerate(s):
            if c=="(":
                stack.append(i)
            elif c==")":
                if stack:
                    stack.pop()
                else:
                    s[i]=""
        while stack:
            s[stack.pop()]=""
        return "".join(s)