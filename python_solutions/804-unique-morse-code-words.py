# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)

"""
Runtime: 36 ms, faster than 77.45% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Morse Code Words.
"""
