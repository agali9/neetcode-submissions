class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1 = 0
        l,r = 0, len(heights)-1
        while l<r:
            max1 = max(max1,min(heights[r],heights[l])*(r-l))
            
            if heights[l]<heights[r]: l+=1
            else: r-=1
        return max1