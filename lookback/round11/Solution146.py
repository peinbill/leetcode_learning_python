#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 01:02
# @Author      : Jim
# @File        : Solution146.py
# @Software    : PyCharm
# @Description :
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # 有序字典，天然维护插入顺序：头部是最久未使用，尾部是最近使用
        self.lru = OrderedDict()
        # 缓存最大容量
        self.max_len = capacity

    def get(self, key: int) -> int:
        # 命中缓存
        if key in self.lru:
            # 移除该键
            value = self.lru.pop(key)
            # 重新插入到字典末尾，标记为最近使用
            self.lru[key] = value
            return value
        # 未命中返回-1
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 键已存在，更新值并更新为最近使用
        if key in self.lru:
            self.lru.pop(key)
            self.lru[key] = value
        else:
            # 容量已满，淘汰最久未使用的元素（头部元素，last=False弹出队首）
            if self.max_len <= len(self.lru):
                self.lru.popitem(last=False)
            # 新增键值，放在尾部，代表最新访问
            self.lru[key] = value