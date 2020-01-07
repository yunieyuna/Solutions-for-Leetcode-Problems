# https://leetcode.com/problems/string-to-integer-atoi/

import re

class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip() # 清楚左边多余空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值
        
"""
Runtime: 32 ms, faster than 66.82% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).
"""
