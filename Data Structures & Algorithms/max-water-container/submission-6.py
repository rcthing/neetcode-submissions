class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxi = 0

        while l < r:
            current = min(heights[l], heights[r]) * (r - l)
            if maxi < current:
                maxi = current

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxi

        