# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 这个题目中，在遍历数组的时候，无非就是这么想：这个房子该不该偷？这么决定的因素是这个房子偷了的话的收益和不偷留着偷下一个房子的收益那个比较高？
        # 也就是说比较这个房子和前前个dp的值的和与前个dp哪个值更大。
        # 整体的思路是当前房间偷和不偷两个状态，如果偷就加上前面第二个偷的商品的状态，如果不偷就是前面一个房间的状态。
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i] + memo[i-1], memo[i])
            print(f"i: {i}")
            print(f"memo: {memo}")

        return memo[len(nums)]