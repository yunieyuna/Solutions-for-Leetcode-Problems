# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rst = []
        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                rst.append("FizzBuzz")
            elif i % 5 == 0:
                rst.append("Buzz")
            elif i % 3 == 0:
                rst.append("Fizz")
            else:
                rst.append(str(i))
        return rst

"""
Runtime: 52 ms, faster than 43.63% of Python3 online submissions for Fizz Buzz.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
"""