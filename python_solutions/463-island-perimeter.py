# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # padding 1
        grid_pad1 = [[0] + row + [0] for row in grid]
        
        # add row at the first
        grid_pad1.insert(0, [0] * (len(grid[0]) + 2))
        # add row at the end
        grid_pad1.append([0] * (len(grid[0]) + 2))
        
        # start slide all window
        rst = 0
        default = 4
        temp = 0

        for r in range(1, len(grid_pad1)-1):
            for c in range(1, len(grid_pad1[0])-1):
                if grid_pad1[r][c] == 0:
                    continue
                if grid_pad1[r][c] == 1:
                    temp = sum([grid_pad1[r+1][c]==1, grid_pad1[r-1][c]==1, grid_pad1[r][c-1]==1, grid_pad1[r][c-1]==1])
                    rst += default - temp
                    
        return rst
        
"""
Runtime: 548 ms, faster than 76.66% of Python3 online submissions for Island Perimeter.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Island Perimeter.
"""
