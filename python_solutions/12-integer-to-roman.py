# https://leetcode.com/problems/integer-to-roman/

# 贪心

class Solution:
    def intToRoman(self, num: int) -> str:
        # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
        # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        index = 0
        res = ''
        while index < 13:
            # 注意：这里是等于号，表示尽量使用大的“面值”
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res
        
"""
Runtime: 52 ms, faster than 41.06% of Python3 online submissions for Integer to Roman.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
"""
