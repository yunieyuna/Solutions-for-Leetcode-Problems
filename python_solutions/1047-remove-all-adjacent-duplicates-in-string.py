# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [0] # 初始化stack，里面放非字母之外任何内容都可以，只为了在第一个stack[-1]时不报错
        for i in S:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack[1:])

"""
Runtime: 64 ms, faster than 94.88% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
"""
