# https://leetcode.com/problems/reverse-string/

# 双指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length < 2:
            return s
        j = length - 1
        i = 0
        while i < j:
            # handle
            s[i], s[j] = s[j], s[i]
            i +=1
            j -=1
        return

"""
Runtime: 220 ms, faster than 77.66% of Python3 online submissions for Reverse String.
Memory Usage: 17.2 MB, less than 98.84% of Python3 online submissions for Reverse String.
"""
