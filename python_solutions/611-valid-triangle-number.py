# https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums, count, n = sorted(nums, reverse=1), 0, len(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count
        
"""
Runtime: 280 ms, faster than 52.71% of Python3 online submissions for Valid Triangle Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Triangle Number.
"""
