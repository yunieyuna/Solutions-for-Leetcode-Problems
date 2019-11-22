# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        # 方法1
        # 首先将该数组从小到达排序，然后依次从第二个数开始，对比其是否与第1个不同且与第3个不同，如果是，则代表该数字为我们要找的。
        
        # 方法2
        # 直接将原数组用set()去重以后，求和并乘2再减去原数组的和，得到single number。

        return 2 * sum(set(nums)) - sum(nums)