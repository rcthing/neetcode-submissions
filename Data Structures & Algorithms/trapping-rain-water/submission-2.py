class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        counter, total = 0, 0

        for r in range(1, len(height)):
            if height[r] >= height[l]:
                total += height[l] * (r - l - 1) - counter
                l = r
                counter = 0
            else:
                counter += height[r]

        r = len(height) - 1
        counter = 0
        for l in range(len(height) - 2, -1, -1):
            if height[l] > height[r]:
                total += height[r] * (r - l - 1) - counter
                r = l
                counter = 0
            else:
                counter += height[l]
        
        return total


            
        