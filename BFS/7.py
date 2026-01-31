#LeetCode Problem 994  Rotting Oranges


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cl, f, r, c=[], 0, len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    cl.append((i,j))
                if grid[i][j]==1:
                    f+=1
        m=0
        while cl and f:
            nl=[]
            for i,j in cl:
                if i>0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    f-=1
                    nl.append((i-1,j))
                if i<r-1 and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    f-=1
                    nl.append((i+1,j))
                if j<c-1 and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    f-=1
                    nl.append((i,j+1))
                if j>0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    f-=1
                    nl.append((i,j-1))
            cl=nl
            m+=1
        return -1 if f else m