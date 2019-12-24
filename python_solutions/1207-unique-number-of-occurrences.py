# https://leetcode.com/problems/unique-number-of-occurrences/

import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = collections.Counter(arr)
        if len(occur.values()) == len(set(occur.values())):
            return True
        else:
            return False
            
"""
Runtime: 28 ms, faster than 98.40% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
"""
