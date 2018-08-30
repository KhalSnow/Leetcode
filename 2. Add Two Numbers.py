# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:09:31 2018

@author: wyh
"""

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

#Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = []
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val
            sum += carry
            res.append(sum % 10)
            carry = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry == 1:
            res.append(1)
        return res