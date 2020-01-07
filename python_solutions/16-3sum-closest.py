# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float("inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right :
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:return target
                if abs(res-target) > abs(cur-target):
                    res = cur
                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
        return res

"""
Runtime: 108 ms, faster than 86.86% of Python3 online submissions for 3Sum Closest.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
"""
