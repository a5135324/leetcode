'''
Detail:

Runtime: 48 ms, faster than 94.95% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 59.12% of Python3 online submissions for Longest Substring Without Repeating Characters.

Submit time: 12/12/2020 14:41 (UTC+8)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        
        ans = 0
        longest_substring = ""
        for i in range(len(s)):
            if i == 0:
                longest_substring = s[i]
                ans = 1
            else:
                if s[i] not in longest_substring:
                    longest_substring = longest_substring + s[i]
                    if len(longest_substring + s[i]) > ans:
                        ans = len(longest_substring)
                else:
                    longest_substring = longest_substring[longest_substring.find(s[i])+1:] + s[i]

        return ans

a = Solution().lengthOfLongestSubstring("abcbdacb")
print(a) # 4
a = Solution().lengthOfLongestSubstring("abcabcbb")
print(a) # 3
a = Solution().lengthOfLongestSubstring("bbbbb")
print(a) # 1
a = Solution().lengthOfLongestSubstring("pwwkew")
print(a) # 3
a = Solution().lengthOfLongestSubstring("")
print(a) # 0

'''
思路：
從左到右一個一個開始找，然後每找下一個的時候看看前一個最長的 substring 有沒有自己。
如過有就把自己以前的東西都拿掉，並把自己加在最後面。
'''
