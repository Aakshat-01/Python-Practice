#LeetCode Problem 227  Basic Calculator II


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        op = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '*':
                    stack.append(stack.pop() * curr)
                elif op == '/':
                    stack.append(int(stack.pop() / curr))
                op = ch
                curr = 0
        return sum(stack)