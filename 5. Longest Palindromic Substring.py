'''
Detail:

Runtime: 3984 ms, faster than 33.67% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 21.5 MB, less than 9.25% of Python3 online submissions for Longest Palindromic Substring.

Submit Time: 2020/03/04 15:55 (UTC+8)
'''

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        
        max_i, max_j = 0, 0
        table = [[False for i in range(n)] for j in range(n)]
        
        for i in range(n):
            table[i][i] = True
            if i != n-1:
                if s[i] == s[i+1]:
                    table[i][i+1] = True
                    max_i = i
                    max_j = i+1
        
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                
                if (table[i+1][j-1] and s[i] == s[j]):
                    table[i][j] = True
                    max_i = i
                    max_j = j


