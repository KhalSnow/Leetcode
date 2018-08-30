# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:22:48 2018

@author: wyh
"""

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point 
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution1:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                l = j - i
                h = min(height[i], height[j])
                maxArea = max(l * h, maxArea)
        return maxArea

class Solution2:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        l = j - i
        h = min(height[i], height[j])
        maxArea = l * h
        while(i < j):
            if height[i] <= height[j]:
                i += 1
                l = j - i
                h = min(height[i], height[j])
                maxArea = max(l * h, maxArea)
            else:
                j -= 1
                l = j - i
                h = min(height[i], height[j])
                maxArea = max(l * h, maxArea)
        return maxArea