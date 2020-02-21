# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        p1, p2 = 0, len(arr) - 1
        while p1 < p2:
            while arr[p1] not in vowel and p1 < p2:
                p1 += 1
            while arr[p2] not in vowel and p1 < p2:
                p2 -= 1
            if p1 < p2:
                arr[p1], arr[p2] = arr[p2], arr[p1]
                p1 += 1
                p2 -= 1
        return ''.join(arr)
        
"""
Runtime: 60 ms, faster than 50.74% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Reverse Vowels of a String.
"""
