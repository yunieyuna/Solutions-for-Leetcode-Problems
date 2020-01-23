# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # refer: https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/er-fen-by-powcai/
        left = 0
        right = len(nums) - 1
        while left <= right:
            # 防止整型溢出
            mid = left + (right - left) // 2
            
            # exit
            if nums[mid] == target:
                return True
            
            # duplicates
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
                
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: # 说明是在右半边的递增区域
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        
"""
Runtime: 48 ms, faster than 90.83% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array II.
"""
