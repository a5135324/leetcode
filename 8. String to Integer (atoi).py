'''
Detail:

Runtime: 36 ms, faster than 53.55% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.3 MB, less than 36.77% of Python3 online submissions for String to Integer (atoi).

Submit time: 12/25/2020 22:17 (UTC+8)
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "" or s == "+" or s == "-":
            return 0
        try:
            ans = int(s)
            if ans <= -2147483648:
                return -2147483648
            elif ans >= 2147483647:
                return 2147483647
            else:
                return ans
        except ValueError:
            ans = 0
            minus = False
            for i in range(len(s)):
                if i == 0:
                    if s[i] == '-':
                        minus = True
                    elif s[i] == '+':
                        pass
                    elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
                        ans = int(s[i])
                    else:
                        return 0
                else:
                    if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                        ans = ans*10 + int(s[i])
                    else:
                        if minus:
                            if ans >= 2147483648:
                                return -2147483648
                            else:
                                return -1*ans
                        else:
                            if ans >= 2147483647:
                                return 2147483647
                            else:
                                return ans
                            

ans = Solution().myAtoi("42")
print(ans) # 42
ans = Solution().myAtoi("   -42")
print(ans) # -42
ans = Solution().myAtoi("4193111111111111111111111111111111111 with words")
print(ans) # 2147483647
ans = Solution().myAtoi("words and 987")
print(ans) # 0
ans = Solution().myAtoi("+-12")
print(ans) # 0
ans = Solution().myAtoi(" ")
print(ans) # 0

'''
思路：
如果只有數字或是空白，python 可以直接透過 int() 轉成數字。
題目又表示如果字串一開始就出現"字母"，就需要回傳 0。(如果是空白或是 +/- 就沒關係。)
所以基本上就是一個字元一個字元讀。
'''