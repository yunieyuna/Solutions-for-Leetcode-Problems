# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        # method 1: brute force
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             count += 1
        # return count
    
        # method 2: 固定起点向后找
        count = 0
        for i in range(len(s)):
            count += 1
            # length is odd
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            # length is even
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
        
        
