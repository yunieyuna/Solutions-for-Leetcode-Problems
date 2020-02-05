# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # sliding windows
        if not nums:
            return 0
        
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0

"""
Runtime: 76 ms, faster than 70.36% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 15 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
"""
