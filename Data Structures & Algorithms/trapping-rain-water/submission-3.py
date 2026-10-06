class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, total = 0, len(height) -1, 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL <= maxR:
                l += 1
                total += max(0, min(maxL, maxR) - height[l])
                if height[l] > maxL:
                    maxL = height[l]
            else:
                r -= 1
                total += max(0, min(maxL, maxR) - height[r])
                if height[r] > maxR:
                    maxR = height[r]
            
        return total


            
        