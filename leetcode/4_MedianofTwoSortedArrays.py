'''

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = len(nums1) + len(nums2)
        medium = tmp // 2
        nums = []
        i1 = i2 = 0
        while i1 + i2 <= medium:
            if i2 > len(nums2) - 1:
                nums.append(nums1[i1])
                i1 += 1
            elif i1 > len(nums1) - 1:
                nums.append(nums2[i2])
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1
        return nums[medium] if tmp % 2 == 1 else (nums[medium] + nums[medium - 1]) / 2
