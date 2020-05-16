# https://leetcode.com/problems/bulb-switcher/

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 除了完全平方数，因数都是成对出现的，这意味着实际起到翻转作用(0->1)的，只有完全平方数而已。
        return int(math.sqrt(n))
        
"""
Runtime: 24 ms, faster than 85.41% of Python3 online submissions for Bulb Switcher.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulb Switcher.
"""
