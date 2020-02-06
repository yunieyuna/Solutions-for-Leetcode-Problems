# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candiate1 = candiate2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == candiate1:
                cnt1 += 1
            elif num == candiate2:
                cnt2 += 1
            elif cnt1 == 0:
                candiate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candiate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [n for n in (candiate1, candiate2) if nums.count(n) > len(nums) // 3]

"""
Runtime: 116 ms, faster than 93.92% of Python3 online submissions for Majority Element II.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Majority Element II.
"""
