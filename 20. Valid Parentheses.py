# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:53:24 2018

@author: wyh
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        maps = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in maps.values():
                stack.append(char)
            elif char in maps.keys():
                if stack == [] or maps[char] != stack.pop():
                    return False
            else:
                return False
        if stack == []:
            return True
        else:
            return False