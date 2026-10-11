class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxr = 0

        for i in range(len(heights)):
            if not stack:
                stack.append((heights[i],i))
            else:
                if heights[i] >= stack[-1][0]:
                    stack.append((heights[i],i))
                else:
                    l = stack[-1][1]
                    while stack and heights[i] < stack[-1][0]:
                        area =  stack[-1][0] * (l - stack[-1][1] + 1)
                        lastIndex = stack[-1][1]
                        maxr = max(maxr, area)
                        stack.pop()
                    stack.append((heights[i],lastIndex))
                    maxr = max(maxr, stack[-1][0] * (i - lastIndex + 1))
        while stack:
            maxr = max(maxr, stack[-1][0] * (len(heights) - stack[-1][1]))
            stack.pop()
                    
        return maxr

            