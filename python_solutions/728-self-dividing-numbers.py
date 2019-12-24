# https://leetcode.com/problems/self-dividing-numbers/

# method 1
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rst = []

        for num in range(left, right+1):

            total = len(str(num))
            count = 0
            for digit in str(num):
                digit = int(digit)
                if digit == 0:
                    continue
                if num % digit == 0:
                    count += 1
            if count == total:
                rst.append(num)
        return rst
        
"""
Runtime: 72 ms, faster than 29.05% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Self Dividing Numbers.
"""
