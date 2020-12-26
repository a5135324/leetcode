'''
Detail:

string
Runtime: 60 ms, faster than 68.33% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 66.77% of Python3 online submissions for Palindrome Number.

int
Runtime: 92 ms, faster than 10.50% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.3 MB, less than 11.54% of Python3 online submissions for Palindrome Number.

Submit time: 12/26/2020 14:05 (UTC+8)
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        forward = []
        backward = []
        while True:
            if x == 0:
                break
            backward.append(x%10)
            forward.insert(0, x%10)
            x = int(x / 10)
        for i in range(len(backward)):
            if backward[i] != forward[i]:
                return False
        return True
                            

ans = Solution().isPalindrome(121)
print(ans) # True
ans = Solution().isPalindrome(-121)
print(ans) # False
ans = Solution().isPalindrome(2147483647)
print(ans) # False
ans = Solution().isPalindrome(121)
print(ans) # True
ans = Solution().isPalindrome(0)
print(ans) # True
ans = Solution().isPalindrome(123321)
print(ans) # True

'''
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True
'''

'''
思路：
解法一 轉成 string，然後前後比。
解法二 把 int 一個一個拆掉存到 list，然後比較內容。
'''