# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        case = abs(ord('a') - ord('A'))
        while left < right:
            while left < right and self.not_letters_digits(s[left]):
                left += 1
            while left < right and self.not_letters_digits(s[right]): 
                right -= 1 
            s_l = ord(s[left]) - case if s[left] >= 'a' else ord(s[left])
            s_r = ord(s[right]) - case if s[right] >= 'a' else ord(s[right])
            if s_l != s_r: 
                return False
            left += 1
            right -= 1
        return True
    
    def not_letters_digits(self, c):
        return not 'A' <= c <= 'Z' and not 'a' <= c <= 'z' and not '0' <= c <= '9'
        
"""
Runtime: 76 ms, faster than 11.39% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.3 MB, less than 76.19% of Python3 online submissions for Valid Palindrome.
"""
