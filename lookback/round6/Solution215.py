#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/16 07:58
# @Author      : Jim
# @File        : Solution215.py
# @Software    : PyCharm
# @Description :

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for i in nums:
            heapq.heappush(pq,i)

            if len(pq)>k:
                heapq.heappop(pq)

        return pq[0]


