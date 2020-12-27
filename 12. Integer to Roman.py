'''
Detail:

Runtime: 44 ms, faster than 84.19% of Python3 online submissions for Integer to Roman.
Memory Usage: 14.2 MB, less than 43.18% of Python3 online submissions for Integer to Roman.

Submit time: 12/27/2020 16:46 (UTC+8)
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = self.convert(int(num/1000), "M", "?", "?")
        num %= 1000
        ans += self.convert(int(num/100), "C", "D", "M")
        num %= 100
        ans += self.convert(int(num/10), "X", "L", "C")
        num %= 10
        ans += self.convert(num, "I", "V", "X")
        return ans

    def convert(self, n, one, five, ten):
        if 3 >= n >= 0:
            return n*one
        elif n == 4:
            return one+five
        elif n == 5:
            return five
        elif n == 9:
            return one+ten
        else:
            return five+(n-5)*one
            

ans = Solution().intToRoman(58)
print(ans) # "LVIII"
ans = Solution().intToRoman(1994)
print(ans) # "MCMXCIV"
ans = Solution().intToRoman(2733)
print(ans) # "MMDCCXXXIII"

'''
思路：
從千位開始轉換。
'''