# https://leetcode.com/problems/shift-2d-grid/submissions/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if  k == 0:
            return grid
        
        m = len(grid)
        n = len(grid[0])
        trow = []
        for row in grid:
            trow += row
        tk = len(trow)
        k = k % tk
        nrow = trow[tk - k: tk] + trow[0: tk - k]
        for i in range(m):
            for j in range(n):
                grid[i][j] = nrow[i * n + j]
        return grid

"""
Runtime: 164 ms, faster than 85.10% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
"""