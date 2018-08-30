# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:38:12 2018

@author: wyh
"""

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i, j = 0, 0
    array = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            array.append(nums1[i])
            i += 1
        else:
            array.append(nums2[j])
            j += 1
    array += nums1[i:]
    array += nums2[j:]
    if len(array) % 2 == 0:
        return (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2
    elif len(array) % 2 == 1:
        return array[len(array) // 2]