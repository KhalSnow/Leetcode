# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:08:22 2018

@author: wyh
"""

"""
Given an array nums and a value val, remove all instances of that value 
in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond 
the new length.
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)