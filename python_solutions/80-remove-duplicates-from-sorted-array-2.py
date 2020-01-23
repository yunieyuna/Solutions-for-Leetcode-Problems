# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1
        
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                
                if count > 2:
                    nums.pop(i)
                    i -= 1
                    
            else:
                count = 1
                
            i += 1
            
        return len(nums)
        
"""
Runtime: 72 ms, faster than 5.94% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array II.
"""
