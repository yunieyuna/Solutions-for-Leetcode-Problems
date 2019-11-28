# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 思路：https://blog.csdn.net/fuxuemingzhu/article/details/79285081#_10

        """
        :type T: List[int]
        :rtype: List[int]
        """
        N = len(T)
        stack = []
        res = [0] * N
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                oi = stack.pop()[1]
                res[oi] = i - oi
            stack.append((t, i))
        return res