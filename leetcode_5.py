# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_5
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
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_start = max_end = 0
        new_start = new_end = 0







def test_main():
    print(Solution().longestPalindrome(''))