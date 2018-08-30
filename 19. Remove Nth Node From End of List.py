# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:37:39 2018

@author: wyh
"""

"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)