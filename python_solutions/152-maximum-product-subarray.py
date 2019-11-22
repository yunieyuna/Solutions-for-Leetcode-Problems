# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, A):
        MinTemp = A[0]
        MaxTemp = A[0]
        Max = A[0]
        for i in range(1, len(A)):
            MinTemp, MaxTemp = min(A[i], A[i] * MaxTemp, A[i] * MinTemp), max(A[i], A[i] * MaxTemp, A[i] * MinTemp)
            Max = max(Max, MaxTemp)
        return Max