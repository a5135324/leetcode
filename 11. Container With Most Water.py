'''
Detail:

Runtime: 196 ms, faster than 9.92% of Python3 online submissions for Container With Most Water.
Memory Usage: 16.5 MB, less than 46.83% of Python3 online submissions for Container With Most Water.

Submit time: 12/26/2020 22:14 (UTC+8)
'''
class Solution:
    def maxArea(self, height: list) -> int:
        left_index = 0
        right_index = len(height)-1
        ans = min(height[left_index], height[right_index]) * abs(left_index-right_index)

        while True:
            if left_index+1 == right_index or left_index == right_index:
                break
            if height[left_index] >= height[right_index]:
                direction = False
            else:
                direction = True
            
            if direction:
                for i in range(left_index, right_index+1):
                    if height[i] > height[left_index]:
                        if min(height[i], height[right_index]) * abs(i-right_index) > ans:
                            ans = min(height[i], height[right_index]) * abs(i-right_index)
                        left_index = i
                        break
            else:
                for i in range(right_index-1, left_index-1, -1):
                    if height[i] >= height[right_index]:
                        if min(height[i], height[left_index]) * abs(i-left_index) > ans:
                            ans = min(height[i], height[left_index]) * abs(i-left_index)
                        right_index = i
                        break

        return ans

ans = Solution().maxArea([4,6,4,4,6,2,6,7,11,2])
print(ans) # 42
ans = Solution().maxArea([1,1])
print(ans) # 1
ans = Solution().maxArea([4,3,2,1,4])
print(ans) # 16
ans = Solution().maxArea([1,2,1,3])
print(ans) # 4
ans = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(ans) # 49
ans = Solution().maxArea([3,9,3,4,7,2,12,6])
print(ans) # 45


'''
思路：
一個一個比，每加入一個就計算一次最大的面積是多少，結果會 TLE。

思路二：
從最寬的開始比，由較小的那邊開始慢慢縮減寬度。
只要出現某個高度比目前最短的柱子高時，計算蓄水量是否會超過當前最大值。
然後不管有沒有比較大，都把最小的高度替換成那個高度(尋找是否有高度較高然後可以讓蓄水量更大的 case)。
'''