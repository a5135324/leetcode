'''
Detail:

Runtime: 56 ms, faster than 77.43% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Min Cost Climbing Stairs.

Submit time: 2020/03/05 15:28 (UTC+8)
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        dp = [0,cost[0]]
                                            
        for i in range(2, n+1):
            dp.append(min(dp[i-2]+cost[i-1], dp[i-1]+cost[i-1]))
                                                                            
        return dp[n]
