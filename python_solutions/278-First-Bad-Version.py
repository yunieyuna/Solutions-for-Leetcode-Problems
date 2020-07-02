# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while right - left > 1:
            if isBadVersion((left + right) // 2):
                right = (left + right) // 2
            else:
                left = (left + right) // 2 + 1
            
        if isBadVersion(left):
            return left
        else:
            return right

        