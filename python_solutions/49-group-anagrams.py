# https://leetcode.com/problems/group-anagrams/

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict ref: https://www.cnblogs.com/mrchige/p/6389985.html
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        
"""
Runtime: 104 ms, faster than 84.64% of Python3 online submissions for Group Anagrams.
Memory Usage: 16.4 MB, less than 47.17% of Python3 online submissions for Group Anagrams.
"""
