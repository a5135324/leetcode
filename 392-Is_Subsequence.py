'''
Detail:

Runtime: 132 ms, faster than 67.91% of Python3 online submissions for Is Subsequence.
Memory Usage: 17.4 MB, less than 26.67% of Python3 online submissions for Is Subsequence.

Submit time: 2020/03/05 17:10 (UTC+8)
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_n = len(s)
        t_n = len(t)
        current = 0
        
        for i in range(s_n):
            check = False
            for j in range(current, t_n):
                if s[i] == t[j]:
                    check = True
                    current = j+1
                    break
            
            if not check:
                return False
        
        return True

