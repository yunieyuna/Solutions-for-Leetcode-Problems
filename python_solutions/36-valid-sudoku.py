# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True
        
"""
Runtime: 96 ms, faster than 75.55% of Python3 online submissions for Valid Sudoku.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Sudoku.
"""
