# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ref: https://blog.csdn.net/L141210113/article/details/89053259
        
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
        
        
```
Result: 

Runtime: 32 ms, faster than 89.56% of Python3 online submissions for Subsets.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Subsets.
```
