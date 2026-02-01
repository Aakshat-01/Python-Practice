#LeetCode Problem 739 Daily Temperatures

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temp)
        for i,t in enumerate(temp):
            while stack and temp[i]>temp[stack[-1]]:
                ind=stack.pop()
                res[ind]=i-ind
            stack.append(i)
        return res