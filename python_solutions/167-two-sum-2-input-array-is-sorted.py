# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        
        while (numbers[left_pointer] + numbers[right_pointer]) != target:
            if (numbers[left_pointer] + numbers[right_pointer]) > target:
                right_pointer -= 1
            if (numbers[left_pointer] + numbers[right_pointer]) < target:
                left_pointer += 1
        return [left_pointer + 1, right_pointer + 1]

"""
Runtime: 60 ms, faster than 89.03% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.
"""