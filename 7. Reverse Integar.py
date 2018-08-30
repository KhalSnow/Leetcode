# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:54:12 2018

@author: wyh
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        a = abs(x)
        while(a != 0):
            pop = a % 10
            rev = rev * 10 + pop
            a = a // 10
        if x > 0 and rev < 2**31:
            return rev
        elif x < 0 and rev <= 2**31:
            return -rev
        else:
            return 0