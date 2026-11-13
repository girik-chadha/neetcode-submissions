class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        if len(prices)==2 and prices[1]-prices[0]>0:
            return prices[1]-prices[0]
        if len(prices)==2 and prices[1]-prices[0]<=0:
            return 0

        
        maxx=0
        minbuy=float('inf')
        for L in range(0,len(prices)-1):
            R=L+1
            minbuy=min(minbuy,prices[L])
            while R<len(prices) and prices[L]<=minbuy:
                if prices[R]-prices[L]>=0:
                    maxx=max(maxx,prices[R]-prices[L])
                    R+=1
                elif prices[R]-prices[L]<0:
                    break
                else:
                    R+=1

        return maxx
            
