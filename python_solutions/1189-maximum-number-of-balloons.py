# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        balloon_dict = {
            'a': 1,
            'b': 1,
            'n': 1,
            'l': 2,
            'o': 2
        }
        result = []
        for key in balloon_dict.keys():
            if key in text_count:
                result.append(int(text_count[key] / balloon_dict[key]))
            else:
                return 0
        return min(result)
        
"""
Runtime: 32 ms, faster than 83.48% of Python3 online submissions for Maximum Number of Balloons.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
"""
