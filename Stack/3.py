#LeetCode Problem 227  Basic Calculator II
#Given a string s which represents an expression, evaluate this expression and return its value cant use any inbuilt function.
#We have to use 2 stack one for digits and one for operators 


class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        curr=0
        dig_stack=[]
        op_stack=[]
        for c in s:
            if c.isdigit():
                dig_stack.append(int(c))
            else:
                if not op_stack or c=='*' or c=="/":
                    op_stack.append(c)
                else:
                    