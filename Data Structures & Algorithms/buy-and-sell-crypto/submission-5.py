class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit

            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
            
        return maxProfit