#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        buy = prices[0]
        sell = prices[0]
        for price in prices:
            if price > sell:
                sell = price
            else:
                bestProfit += sell - buy
                buy = price
                sell = price

        if sell - buy > 0:
            bestProfit += sell - buy

        return bestProfit

# Time: O(n)
# Space: O(1)