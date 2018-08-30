# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:47:59 2018

@author: wyh
"""

"""
Given an array nums containing n + 1 integers where each integer is between 1 
and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return nums[i]
                