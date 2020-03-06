'''
Detail:

Runtime: 20 ms, faster than 98.54% of Python3 online submissions for House Robber.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for House Robber.

Submit time: 2020/03/06 13:37(UTC+8)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0,0,0]
        ans = 0
        
        for i in range(3,n+3):
            dp.append(max(dp[i-3]+nums[i-3], dp[i-2]+nums[i-3]))
            if dp[i] > ans:
                ans = dp[i]
        
        return ans

