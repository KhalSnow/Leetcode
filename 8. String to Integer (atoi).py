# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:48:43 2018

@author: wyh
"""

"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the 
first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral 
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty or 
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
If the numerical value is out of the range of representable values, 
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        str = re.findall('^[+\-]?\d+', str)

        try:
            res = int(''.join(str))
            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN: 
                return MIN
            return res
        except: 
            return 0