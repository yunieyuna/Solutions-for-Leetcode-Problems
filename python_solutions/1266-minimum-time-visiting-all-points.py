# https://leetcode.com/problems/minimum-time-visiting-all-points/

# method 1
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        curr = points[0]
        count = 0

        for i in range(len(points)):
            while curr != points[i]:
                # x axis
                if curr[0] < points[i][0]:
                    curr[0] += 1
                if curr[0] > points[i][0]:
                    curr[0] -= 1

                # y axis
                if curr[1] < points[i][1]:
                    curr[1] += 1
                if curr[1] > points[i][1]:
                    curr[1] -= 1

                count += 1

        return count
        
"""
Runtime: 2836 ms, faster than 5.02% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
"""

# method 2
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x0, x1 = points[0]
        ans = 0
        
        for i in range(1, len(points)):
            y0, y1 = points[i]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = points[i]
        return ans
        
"""
Runtime: 60 ms, faster than 54.50% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
"""
