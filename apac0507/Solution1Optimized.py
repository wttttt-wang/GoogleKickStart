#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/7 15:13
# @Author  : wttttt
# @Github  : https://github.com/wttttt-wang/leetcode
# @Site    : 
# @File    : Solution1Optimized.py
# @Software: PyCharm
# @Desc:

class Solution(object):
    def solution(self):
        f = open('input/A-large-practice.in.txt')
        o = open('input/resultLargestOptimized.out', 'w+')
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
        localBefore, sumBefore, sum = 0, 0, 0
        factor, val = 1, 1
        for i in range(1, len(numbers)):
            local = localBefore * 2 + (int(numbers[i]) - int(numbers[i - 1])) * val
            factor *= 2
            val += factor
            val %= 1000000007
            sum = sumBefore + local
            localBefore, sumBefore = local % 1000000007, sum % 1000000007
        return sum % 1000000007


import time
before = time.time()
so = Solution()
so.solution()
print time.time() - before