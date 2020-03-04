'''
Details

Runtime: 60 ms, faster than 83.15% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.

Submit Time: 2020/03/04 12:01 (UTC+8)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        if len(prices) > 0:
            low = prices[0]
            for x in range(1,len(prices)):
                if prices[x] < low:
                    low = prices[x]
                if prices[x] - low > ans:
                    ans = prices[x] - low
        
        return ans
