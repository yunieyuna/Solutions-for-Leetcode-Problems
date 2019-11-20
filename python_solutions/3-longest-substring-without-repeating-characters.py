# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        longest_str = []
        for element in s:
            if element in longest_str:
                return len(longest_str)
            longest_str.append(element)
        return len(longest_str)
