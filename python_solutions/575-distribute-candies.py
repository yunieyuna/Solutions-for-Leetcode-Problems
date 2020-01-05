# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        length = len(candies)
        each = length // 2
        candies.sort()
        count = 1
        for i in range(1, length):
            if candies[i] != candies[i - 1]:
                count += 1
        return each if each <= count else count

"""
Runtime: 1020 ms, faster than 7.94% of Python3 online submissions for Distribute Candies.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Distribute Candies.
"""