# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:27:25 2018

@author: wyh
"""

"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.
"""

#Brute Force O(n^3)
def isPalindromic(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
        else:
            return True
def longestPalindrome(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    maxLen = 0
    ans = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            test = s[i:j]
            if (isPalindromic(test) and len(test) > maxLen):
                ans = s[i:j]
                maxLen = max(maxLen, len(ans))
    return ans, maxLen
if __name__ == "__main__":
    print(longestPalindrome(str("abbac")))


#Dynamic Programming Time:O(n^2) Space:O(n^2)
def longestPalindrome(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    maxLen = 0
    ans = ""
    start, end = 0, 0
    dp = [[False] * len(s) for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            dp[i][i + 1] = True
            start = i
            end = i + 1
        else:
            dp[i][i + 1] = False
    for l in range(3, len(s) + 1):
        for i in range(len(s) - l + 1):
            j = i + l - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                end = j
            else:
                dp[i][j] = False
    ans = s[start:end + 1]
    maxLen = end - start + 1
    return ans, maxLen
if __name__ == "__main__":
    print(longestPalindrome(str("cbbd")))


#中心展开 Time:O(n^2) Space:O(n)
def longestPalindrome(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    maxLen = 0
    ans = ""
    start, end = 0, 0
    #长度为奇数
    for i in range(len(s)):
        j = i - 1
        k = i + 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            if k - j + 1 > maxLen:
                maxLen = k - j + 1
                start = j
                end = k
            j -= 1
            k += 1
    #长度为偶数
    for i in range(len(s)):
        j = i
        k = i + 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            if k - j + 1 > maxLen:
                maxLen = k - j + 1
                start = j
                end = k
            j -= 1
            k += 1
    ans = s[start:end + 1]
    return ans, maxLen
if __name__ == "__main__":
    print(longestPalindrome(str("cbbd")))