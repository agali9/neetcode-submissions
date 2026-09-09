class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_Area = 0
        stack = []
        for n in range(len(heights)):
            start = n
            while stack and heights[n] < stack[-1][1]:
                i, height = stack.pop()
                max_Area = max(max_Area,height*(n-i))
                start = i
            stack.append((start,heights[n]))
        for i, h in stack:
            max_Area = max(max_Area, h*(len(heights)-i))
        return max_Area
