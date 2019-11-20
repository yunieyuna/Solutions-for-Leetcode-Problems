# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        len_height = len(height)
        if len_height < 2:
            return 0
        max_area = 0
        i = 0
        j = len_height - 1
        while i != j:
            h = min(height[i], height[j])
            w = j - i
            if max_area < h * w:
                max_area = h * w
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return max_area
