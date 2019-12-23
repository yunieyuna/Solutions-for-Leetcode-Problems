# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        count_L = 0
        count_R = 0
        
        for s_ in s:
            if s_ == 'L':
                count_L += 1
            else:
                count_R += 1
            if count_L == count_R:
                count += 1
        return count

"""
Runtime: 28 ms, faster than 86.49% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
"""
