# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 11:03:25 2018

@author: wyh
"""

"""
Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s) - 1):
            