'''
Detail:

Runtime: 24 ms, faster than 83.95% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

Submit Date: 2020/03/03 23:30 (UTC+8)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        num = [1,1]
        for x in range(1, n):
            num.append(num[x]+num[x-1])
        return num[n]
