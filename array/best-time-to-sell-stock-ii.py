# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevPrice = prices[0]
        profit = 0

        for price in prices:
            if price > prevPrice:
                profit += price - prevPrice
            
            prevPrice = price

        return profit
    
"""
I overthought this one at first.

Ultimately, we can use the greedy algorithm, as if we have
1,3,5 it doesn't matter if we do +2+2 or +4 for buying and selling
stocks. As a result we can just keep adding profits while the
stocks go up and make sure to sell when it stops going up, waiting
until it stops going down to buy/sell again.

O(n) time
"""