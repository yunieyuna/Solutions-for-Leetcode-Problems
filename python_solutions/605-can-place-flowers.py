# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 首尾补0
        nums = [0] + flowerbed + [0]
        
        count = 0
        i = 1
        while i < len(flowerbed) + 1:
            if nums[i-1] == 0 and nums[i] == 0 and nums[i+1] == 0:
                count += 1
                i += 2
            else:
                i += 1
                
        return count >= n
        
"""
Runtime: 176 ms, faster than 70.31% of Python3 online submissions for Can Place Flowers.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.
"""
