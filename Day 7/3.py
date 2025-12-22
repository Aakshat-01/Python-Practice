class Solution(object):
    def maxArea(self, height):
        n=len(height)
        max_a=0
        i=0
        j=n-1
        while(i<j):
            h=min(height[i],height[j])
            l=j-i
            a=h*l
            max_a=max(max_a,a)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_a
