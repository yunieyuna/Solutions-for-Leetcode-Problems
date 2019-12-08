# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
