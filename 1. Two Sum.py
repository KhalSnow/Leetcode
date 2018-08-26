# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:38:43 2018

@author: wyh
"""

"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice. 
"""

class Solution:
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            else:
                dic[target - num] = index

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]