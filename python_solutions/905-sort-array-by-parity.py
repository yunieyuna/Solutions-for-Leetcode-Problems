# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ##  Answer 1
        odd = []
        even = []
        for element in A:
            if element % 2 == 0:
                even.append(element)
            else:
                odd.append(element)
        return even + odd
