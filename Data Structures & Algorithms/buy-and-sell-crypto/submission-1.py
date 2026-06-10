class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]      
        ma = 0             
        
        for i in range(1, len(prices)):
            if prices[i] < m:
                m = prices[i]  
            elif prices[i] - m > ma:
                ma = prices[i] - m  
        
        return ma

            
        