# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_4
   Description :
   Author :       xpzhao
   date：          18-5-15
-------------------------------------------------
   Change Activity:
                   18-5-15:
-------------------------------------------------
"""
__author__ = 'xpzhao'

"""
        给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
        
        请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
        
        示例 1:
        
        nums1 = [1, 3]
        nums2 = [2]
        
        中位数是 2.0
        
        示例 2:
        
        nums1 = [1, 2]
        nums2 = [3, 4]
        
        中位数是 (2 + 3)/2 = 2.5

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()

        length = len(nums)
        if length == 0:
            return None
        elif length% 2 == 0:
            return (nums[int(length/2) -1] + nums[int(length/2)])/2
        else:
            return nums[int(length/2)]

def test_main():
    print(Solution().findMedianSortedArrays([1,1],[1,2]))