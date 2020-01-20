# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # if the starting cell has an obstacle, then simply return as there would be no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Number of ways of reaching the starting cell = 1
        obstacleGrid[0][0] = 1
        
        # Filling the values for the first column
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
            
        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
            
        # Starting from cell(1,1) fill up the values
        # No# of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        # return value stored in rightmost bottommost cell.
        return obstacleGrid[m-1][n-1]
        
"""
时间复杂度 ： O(M×N) 。长方形网格的大小是 M×N，而访问每个格点恰好一次。
空间复杂度 ： O(1)。我们利用 obstacleGrid 作为 DP 数组，因此不需要额外的空间。
"""
