#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/7 12:34
# @Author  : wttttt
# @Github  : https://github.com/wttttt-wang
# @Site    : 
# @File    : Solution2.py
# @Software: PyCharm
# @Desc:

def solution():
    f = open('input/B-large-practice.in.txt')
    o = open('input/resultLargeB.out', 'w+')
    lineCnt = 1
    for i in range(int(f.readline())):
        # handling each input
        pointsNum = int(f.readline())
        data, data2 = [], []
        for j in range(pointsNum):
            data.append([float(ele) for ele in f.readline().strip().split()])
        # coordinate transformation
        for x, y, w in data:
            data2.append([(x + y) / 2, (x - y) / 2, w])
        u = median(list(map(lambda x: [x[0], x[2]], data2)))
        v = median(list(map(lambda x: [x[1], x[2]], data2)))

        xs, ys = u + v, u - v
        ans = sum([max(abs(x - xs), abs(y - ys)) * w for x, y, w in data])

        print xs, ys
        print("Case #%d: %f" % (lineCnt, ans))
        o.write('Case #%d: %s' % (lineCnt, ans) + '\n')
        lineCnt += 1


def median(data):
    data = sorted(data)
    s = sum(map(lambda x: x[1], data)) / 2.0
    for a, b in data:
        if s <= b: return a
        s -= b

solution()
