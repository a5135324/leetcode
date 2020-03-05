'''
Detail:

Runtime: 76 ms, faster than 88.34% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.

Submit time: 2020/03/05 17:32 (UTC+8)
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        for x in range(1,n):
            nums[x] += nums[x-1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums[j]
        else:
            return (self.nums[j] - self.nums[i-1])

