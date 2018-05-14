# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_3
   Description :
   Author :       xpzhao
   date：          18-5-14
-------------------------------------------------
   Change Activity:
                   18-5-14:
-------------------------------------------------
"""
__author__ = 'xpzhao'


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_start = 0
        max_end = 1
        new_start = 0
        new_end = 1

        i = 1;
        length = len(s)

        if length == 0:
            return 0

        while i < length:
            c = s[i]
            i += 1
            if c in s[new_start:new_end]:
                # c存在于子串
                #print(c, s[new_start:new_end])

                # 更新max
                if new_end - new_start > max_end - max_start:
                    max_start = new_start
                    max_end = new_end

                for j in range(new_start, new_end):
                    if c == s[j]:
                        # position i same with c, update new_start to i
                        new_start = j + 1
                new_end += 1
                #print('new substr', new_start, new_end, s[new_start:new_end])
            else:
                new_end += 1

        if new_end - new_start > max_end - max_start:
            max_start = new_start
            max_end = new_end

        #print(max_end, max_start, s[max_start:max_end])
        return max_end - max_start


def test_main():
    Solution().lengthOfLongestSubstring('abcadeefhigklmn')