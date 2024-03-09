#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 01:20
# @Author      : Jim
# @File        : Solution146.py
# @Software    : PyCharm
# @Description : 反正就是怎么都要pop出来，无论存在还是不存在
# https://www.cnblogs.com/ajianbeyourself/p/4555560.html

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.max_len = capacity

    def get(self, key: int) -> int:
        if key in self.lru:
            value = self.lru.pop(key)
            self.lru[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            _ = self.lru.pop(key)
            self.lru[key] = value
        else:
            if self.max_len <= len(self.lru):
                self.lru.popitem(last=False)

            self.lru[key] = value


