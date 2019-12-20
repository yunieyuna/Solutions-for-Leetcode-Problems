# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 排序后遍历
        arr.sort()
        substract_list = [(arr[m] - arr[m-1]) for m in range(1, len(arr))]
        minsub = min(substract_list)
        
        lists = []
        for t in range(len(substract_list)):
            if substract_list[t] == minsub:
                lists.append([arr[t], arr[t+1]])
        return lists
        
"""
Runtime: 356 ms, faster than 97.19% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 26.6 MB, less than 100.00% of Python3 online submissions for Minimum Absolute Difference.
"""
