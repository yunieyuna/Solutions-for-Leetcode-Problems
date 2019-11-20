class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create dict for store nums
        dict_for_store = {}
        
        for index, num1 in enumerate(nums):
            
            num2 = target - num1
            
            if num2 in dict_for_store:
                return [dict_for_store[num2], index]
            else:
                dict_for_store[num1] = index
