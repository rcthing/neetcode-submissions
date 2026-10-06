class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0, 0 
        max = 0
        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i
                high = i
            if prices[i] >= prices[high]:
                high = i
            if prices[high] - prices[low] > max:
                max = prices[high] - prices[low]

        return max