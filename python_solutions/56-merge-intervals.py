# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # https://leetcode-cn.com/problems/merge-intervals/solution/pai-xu-by-powcai/
        
        # 1. 先按首位置进行排序
        intervals = sorted(intervals)
        
        # 2. 接下来,如何判断两个区间是否重叠呢?比如 a = [1,4],b = [2,3], 当 a[1] >= b[0] 说明两个区间有重叠
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            # 3. 左边位置一定是确定，就是 a[0]，而右边位置是 max(a[1], b[1])
            while i < n - 1 and intervals[i+1][0] <= right:
                i += 1
                right = max(intervals[i][1], right)
            res.append([left, right])
            i += 1
        return res
        
"""
Runtime: 92 ms, faster than 38.28% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
"""
