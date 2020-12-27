'''
Detail:

Runtime: 40 ms, faster than 92.00% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.4 MB, less than 17.77% of Python3 online submissions for Roman to Integer.

Submit time: 12/27/2020 16:46 (UTC+8)
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        if s.find("CM") != -1:
            ans += 900
            s = s.replace("CM", "")
        elif s.find("CD") != -1:
            ans += 400
            s = s.replace("CD", "")
        if s.find("XC") != -1:
            ans += 90
            s = s.replace("XC", "")
        elif s.find("XL") != -1:
            ans += 40
            s = s.replace("XL", "")
        if s.find("IX") != -1:
            ans += 9
            s = s.replace("IX", "")
        elif s.find("IV") != -1:
            ans += 4
            s = s.replace("IV", "")
        
        for i in s:
            if i == "M":
                ans += 1000
            elif i == "D":
                ans += 500
            elif i == "C":
                ans += 100
            elif i == "L":
                ans += 50
            elif i == "X":
                ans += 10
            elif i == "V":
                ans += 5
            elif i == "I":
                ans += 1

        return ans
            

ans = Solution().romanToInt("MCMXCIV")
print(ans) # 1994
ans = Solution().romanToInt("MMDCCXXXIII")
print(ans) # 2733

'''
思路：
暴力轉換。
'''