# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cur, cnt = arr[0], 0
        for i in range(n):
            if arr[i] == cur:
                cnt += 1
                if cnt * 4 > n:
                    return cur
            else:
                cur, cnt = arr[i], 1
        return -1

"""
Runtime: 92 ms, faster than 79.85% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
"""