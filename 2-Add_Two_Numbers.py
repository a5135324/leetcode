'''
Detail:

Runtime: 80 ms, faster than 19.86% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

Submit time: 2020/03/06 14:44 (UTC+8)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        times = 0
        val_1, val_2 = 0,0
        while l1:
            val_1 += l1.val * (10**times)
            times+=1
            l1 = l1.next
        
        times = 0
        while l2:
            val_2 += l2.val * (10**times)
            times+=1
            l2 = l2.next
            
        _sum = val_2+val_1
        
        ans = ListNode()
        current = ans
        current.val = _sum%10
        _sum = _sum//10
        while _sum:
            temp = ListNode()
            temp.val = _sum%10
            current.next = temp
            current = temp
            _sum = _sum//10
        
        return ans

