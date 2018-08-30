# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:26:21 2018

@author: wyh
"""

"""
Given an array nums of n integers, are there elements a, b, c in nums such that 
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            s, e = i+1, n-1
            while s < e:
                if nums[s] + nums[e] == target:
                    res.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return res