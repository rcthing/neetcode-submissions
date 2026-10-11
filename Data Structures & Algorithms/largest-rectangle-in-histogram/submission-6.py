class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                he, index = stack.pop()
                start = index
                maxA = max(maxA, he * (i - index))
            
            stack.append((heights[i],start))
                
        for h in stack:
            maxA = max(maxA, h[0] * (len(heights) - h[1]))
                    
        return maxA

            