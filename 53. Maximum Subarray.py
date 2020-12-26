'''
Detail:

Runtime: 64 ms, faster than 82.68% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 59.35% of Python3 online submissions for Maximum Subarray.

Submit Time: 2020/03/03 17:30 (UTC+8)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        ans = nums[0]
        
        for x in range(1,len(nums)):
            if (nums[x] + dp[x-1]) > nums[x]:
                dp.append(nums[x]+dp[x-1])
            else:
                dp.append(nums[x])
            if dp[x] > ans:
                ans = dp[x]
        
        return ans
