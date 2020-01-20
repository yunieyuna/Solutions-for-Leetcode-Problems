# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
        def dfs(n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index + 1, path)
                
        if n == 0:
            return ""
        
        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])
        
"""
Runtime: 32 ms, faster than 36.56% of Python3 online submissions for Permutation Sequence.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutation Sequence.
"""
