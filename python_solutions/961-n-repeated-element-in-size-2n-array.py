# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


# method 1
import collections

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # method 1
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
                
"""
Runtime: 220 ms, faster than 90.15% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 14 MB, less than 95.92% of Python3 online submissions for N-Repeated Element in Size 2N Array.
"""


# method 2
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # method 2
        temp = set()
        for i in A:
            if i not in temp:
                temp.add(i)
            else:
                return i
                
"""
Runtime: 232 ms, faster than 77.53% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 14 MB, less than 93.88% of Python3 online submissions for N-Repeated Element in Size 2N Array.
"""
