# https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies > i:
            ans[i % num_people] += i + 1
            candies -= i + 1
            i += 1
        ans[i % num_people] += candies
        return ans

"""
Runtime: 32 ms, faster than 85.04% of Python3 online submissions for Distribute Candies to People.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.
"""