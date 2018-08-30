# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:57:03 2018

@author: wyh
"""

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. 
Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        left = num
        list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        maps = {5: "V", 1: "I", 10:"X", 50: "L", 100: "C", 500:"D", 1000: "M", 4:"IV", 9:"IX", 90:"XC", 400:"CD", 900:"CM", 40:"XL"}
        while left > 0:
            for k in list:
                if left >= k:
                    res += maps[k]
                    left -= k
                    break
        return res