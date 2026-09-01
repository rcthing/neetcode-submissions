class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue

            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit

            
            
        return maxProfit