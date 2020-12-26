'''
Detail:

Runtime: 72 ms, faster than 28.28% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.4 MB, less than 22.70% of Python3 online submissions for ZigZag Conversion.

Submit time: 12/12/2020 17:28 (UTC+8)
'''

from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = defaultdict(list)
        next_ = 0
        sign = 1
        for i in range(len(s)):
            zigzag[next_].append(s[i])
            if next_ == numRows-1:
                sign = 0
            elif next_ == 0:
                sign = 1
            if sign:
                next_ += 1
            else:
                next_ -= 1

        ans = ''
        for i in range(numRows):
            for j in zigzag[i]:
                ans += j
        
        return ans

a = Solution().convert("AB", 1)
print(a) # A
a = Solution().convert("PAYPALISHIRING", 3)
print(a) # PAHNAPLSIIGYIR
a = Solution().convert("PAYPALISHIRING", 4)
print(a) # PINALSIGYAHRPI
'''
思路：
一個字一個字放進 list，之後輸出。
'''