class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxi = 0

        while l < r:
            maxi = max(min(heights[l], heights[r]) * (r - l), maxi)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxi