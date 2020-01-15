# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= last-i:
                last = i
        if last == 0:
            return True
        return False

"""
Runtime: 92 ms, faster than 62.95% of Python3 online submissions for Jump Game.
Memory Usage: 14.9 MB, less than 7.14% of Python3 online submissions for Jump Game.
"""
