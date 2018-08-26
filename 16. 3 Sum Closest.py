# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:09:12 2018

@author: wyh
"""

"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
"""
nums = [-1,2,1,-4,3,9]
target = 5
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closest = []
        for i, num in enumerate(nums[0:-2]):
            l,r = i+1, length-1
            if num + nums[r] + nums[r-1] < target:
                closest.append(num + nums[r] + nums[r-1])
            elif num + nums[l] + nums[l+1] > target:
                closest.append(num + nums[l] + nums[l+1])
            else:
                while l < r:
                    closest.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        return target
        closest.sort(key = lambda x:abs(x - target))
        return closest[0]