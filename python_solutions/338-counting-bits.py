# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: int) -> List[int]:
        # method 1: brute force
        rst = []
        for i in range(num + 1):
            rst.append(bin(i).count('1'))
        return rst

        # # method 2: 通过观察前10个数的二进制，可以发现：[2-3]中1的个数是[0-1]中个数对应加一；[4-7]是[0-3]对应加一；[8-15]是[0-7]对应加一；
        # # 本质上，是将最高位的1变成0得到对应的较小的数。 (https://blog.csdn.net/coder_orz/article/details/52063216)
        # dp = [0, 1]
        
        # while len(dp) <= num:
        #     dp.extend(map(lambda x: x+1, dp))
            
        # return dp[:num + 1]
