# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:41:19 2018

@author: wyh
"""

"""
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.
"""
nums = [1, 0, -1, 0, -2, 2]
target = 0

"""
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        array = []
        for i, num in enumerate(nums):
            l,r = i+1, length-1
            j = l + 1
            if num + nums[r-2] + nums[r-1] + nums[r] > target:
                continue
            elif num + nums[r-2] + nums[r-1] + nums[r] == target:
               array.append([num, nums[r-2], nums[r-1], nums[r]])
            elif num + nums[l] + nums[l+1] + nums[l+2] < target:
                continue
            elif num + nums[l] + nums[l+1] + nums[l+2] == target:
                array.append([num, nums[l], nums[l+1], nums[l+2]])
            else:
                while l < r:
                    if num + nums[l] + nums[j] + nums[r] < target:
                        
                        array.append([num, nums[l], nums[j], nums[r]])
                    else:
                        j += 1
        return array