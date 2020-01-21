# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num2 = num2[::-1]
        num1 = num1[::-1]
        lenNum = len(num1) + len(num2) # 保存最终最大的数字
        returnNum = [0 for c in range(lenNum)] # 用list先存储
        
        for index2 in range(len(num2)):
            multiplier2 = int(num2[index2]) # 就直接按照顺序放，最后再反过来！
            for index1 in range(len(num1)):
                multiplier1 = int(num1[index1])
                temp = multiplier2 * multiplier1 + returnNum[index1 + index2]
                if temp >= 10:
                    returnNum[index1 + index2] = temp % 10
                    returnNum[index1 + index2 + 1] += int(temp / 10)
                else:
                    returnNum[index1 + index2] = temp
                    
        returnNum = returnNum[::-1]
        while returnNum and returnNum[0] == 0:
            del returnNum[0]
        returnNum = [str(c) for c in returnNum]
        
        return ''.join(returnNum)

"""
Runtime: 128 ms, faster than 46.43% of Python3 online submissions for Multiply Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Multiply Strings.
"""
