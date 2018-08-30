# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:51:18 2018

@author: wyh
"""

"""
Given an array nums of n integers where n > 1,  return an array output such 
that output[i] is equal to the product of all the elements of nums except nums[i].
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        res = []
        for i in range(n):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res