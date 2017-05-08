#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/7 12:34
# @Author  : wttttt
# @Github  : https://github.com/wttttt-wang
# @Site    : 
# @File    : Solution1.py
# @Software: PyCharm
# @Desc:

class Solution(object):
    def solution(self):
        f = open('input/A-large.in.txt')
        o = open('input/resultLargest.out', 'w+')
        lineCnt = 1
        f.readline()
        while f.readline():
            ans = self.encode(f.readline().replace("\n", "").strip().split())
            o.write('Case #%d: %s' % (lineCnt, ans) + '\n')
            lineCnt += 1
        f.close()
        o.close()

    def encode(self, numbers):
        if not numbers:
            return 0
        ans = 0
        for i in range(len(numbers) - 1):
            factor = 1
            for j in range(i + 1, len(numbers)):
                ans += (int(numbers[j]) - int(numbers[i])) * factor
                ans %= 1000000007
                factor *= 2
                factor %= 1000000007
        return ans % 1000000007

import time
before = time.time()
so = Solution()
so.solution()
print time.time() - before

