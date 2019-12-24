# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i - prev)
            
        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev-i)
            
        return ans
        
"""
Runtime: 40 ms, faster than 79.18% of Python3 online submissions for Shortest Distance to a Character.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Shortest Distance to a Character.
"""
