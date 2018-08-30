# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:47:39 2018

@author: wyh
"""

"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False