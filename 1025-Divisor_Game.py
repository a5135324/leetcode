'''
Detail:

Runtime: 28 ms, faster than 70.97% of Python3 online submissions for Divisor Game.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Divisor Game.
    
Submit Time: 2020/03/04 16:39 (UTC+8)
'''

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N%2 == 0:
            return True
    else:
            return False
