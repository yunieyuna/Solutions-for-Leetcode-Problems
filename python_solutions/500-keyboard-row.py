# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')

        rst = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx <= set1 or setx <= set2 or setx <= set3:
                rst.append(i)
        return rst
        
"""
Runtime: 36 ms, faster than 42.59% of Python3 online submissions for Keyboard Row.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Keyboard Row.
"""
