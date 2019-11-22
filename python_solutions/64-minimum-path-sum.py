# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Dynamic Programming
        m = len(grid) # height
        n = len(grid[0]) # width
        for i in range(1, n):
            grid[0][i] += grid[0][i-1] # one side is wall
        for i in range(1, m):
            grid[i][0] += grid[i-1][0] # one side is wall
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) # get minimum from left or above
        return grid[i-1][j-1]