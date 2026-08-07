class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        
        # prices=[7, 1, 5, 3, 6, 4]
        while r < len(prices):
            
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r+=1
        
        return res