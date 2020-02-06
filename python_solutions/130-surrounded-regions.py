# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # ref: https://leetcode-cn.com/problems/surrounded-regions/solution/dfs-bfs-bing-cha-ji-by-powcai/
        
        if not board or not board[0]:
            return 
        row = len(board)
        col = len(board[0])
        
        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)
                    
        for j in range(col):
            if board[0][j] == "O":
                dfs(0, j)
            if board[row - 1][j] == "O":
                dfs(row - 1, j)
                
        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

"""
Runtime: 136 ms, faster than 96.25% of Python3 online submissions for Surrounded Regions.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Surrounded Regions.
"""