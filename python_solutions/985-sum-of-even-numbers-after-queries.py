# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        rst = []
        for i in range(len(queries)):
            A[queries[i][1]] += queries[i][0]
            rst.append(sum([x for x in A if x % 2 == 0]))
        return rst
