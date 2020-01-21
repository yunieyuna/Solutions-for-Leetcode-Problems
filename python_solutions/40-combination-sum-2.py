# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return
            
            for index in range(begin, size):
                if candidates[index] > residue:
                    break
                    
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue
                
                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()
                
        size = len(candidates)
        if size == 0:
            return []
        
        candidates.sort()
        res = []
        dfs(0, [], target)
        return res
        
"""
Runtime: 48 ms, faster than 78.34% of Python3 online submissions for Combination Sum II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum II.
"""
