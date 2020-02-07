# https://leetcode.com/problems/circular-array-loop/

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        # 实现思路：
        # 循环1：以数组的每个点为起点，开始循环。
        # 循环2：将路径点加入到set中，并更新新的位置
        # 判断set中的路径是否有效：
        # (1)出现反向时，路径无效
        # (2)循环长度为1时，路径无效
        # (2)循环长度>1, 且出现环, 路径有效

        
        n = len(nums)
        for start in range(n):
            s = set()
            pos = start
            posLast = pos
            flag = 0
            while pos not in s:
                flag = 1
                s.add(pos)
                posLast = pos
                pos = (pos + nums[pos] + n) % n
                if nums[pos] * nums[start] < 0:
                    flag = 2
                    break
            
            if pos == posLast:
                continue
            if len(s) > 1 and flag == 1:
                return True
            
        return False

"""
Runtime: 500 ms, faster than 34.21% of Python3 online submissions for Circular Array Loop.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Circular Array Loop.
"""
