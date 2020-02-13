# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 使用哈希映射记录每个字母的转换方法，键：s的字母，值：t的字母
        hash_map = {}
        
        # 由于s和t具有相同的长度，所以使用zip遍历
        for c1, c2 in zip(s, t):
            
            # 如果c1已在键中，且c2与键c1的值不对应，说明出现了s=aa，t=ab这种情况
            if c1 in hash_map and c2 != hash_map[c1]:
                return False
            
            # 如果c1不在键中，但c2出现在字典的值中，说明出现了s=ab，t=aa这种情况
            if c1 not in hash_map and c2 in hash_map.values():
                return False
            
            # 仅有以上两种情况需要输出False，如果不满足以上两种情况，则添加键值对
            hash_map[c1] = c2
            
        # 循环走完说明s和t中每个字母都有唯一的对应关系，可以输出True
        return True
        
"""
Runtime: 28 ms, faster than 97.72% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Isomorphic Strings.
"""
