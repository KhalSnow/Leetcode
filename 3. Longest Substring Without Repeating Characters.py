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
        maxLen = 0
        maps = {}
        start = 0
        for i in range(len(s)):
            position = maps.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                maxLen = max(length, maxLen)
            maps[s[i]] = i
        maxLen = max(len(s) - start, maxLen)
        return maxLen
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("bbbbbb"))
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("abcabcbb1234567"))
    print(solution.lengthOfLongestSubstring("cdd"))
    print(solution.lengthOfLongestSubstring("dvdf"))
    print(solution.lengthOfLongestSubstring("pwwkew"))