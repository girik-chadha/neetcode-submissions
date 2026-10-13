class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L,R = 0,1
        min_price = float("inf")
        max_profit=0

        while R<len(prices):
            if prices[R]-prices[L]>0:
                max_profit = max(max_profit, prices[R] - prices[L])
                R+=1
            else:
                L+=1
                R=L+1
        return max_profit
