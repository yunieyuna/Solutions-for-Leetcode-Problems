# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # reference: https://blog.csdn.net/coder_orz/article/details/52075042
        
        data = {}
        res = []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        bucket = [[] for i in range(len(nums) + 1)]
        for key in data:
            bucket[data[key]].append(key)
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]