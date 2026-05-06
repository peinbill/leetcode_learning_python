#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/5 22:18
# @Author      : Jim
# @File        : Solution146.py
# @Software    : PyCharm
# @Description :
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # 有序字典：天然维护插入/访问时序
        # 头部：最久未使用；尾部：最近使用
        self.lru = OrderedDict()
        # 缓存最大容量
        self.max_len = capacity

    def get(self, key: int) -> int:
        # 命中key
        if key in self.lru:
            # 先弹出，再重新插入 -> 移到末尾(标记为最近使用)
            value = self.lru.pop(key)
            self.lru[key] = value
            return value
        # 未命中返回-1
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # key已存在：删除旧数据，重新插入刷新时序
        if key in self.lru:
            self.lru.pop(key)
            self.lru[key] = value
        else:
            # 超出容量：淘汰最久未使用(头部元素 last=False)
            if len(self.lru) >= self.max_len:
                self.lru.popitem(last=False)
            # 新增键值对，放在末尾
            self.lru[key] = value


# 定义双向链表的节点类
class Node:
    def __init__(self, key, val):
        self.key = key  # 存储 key（淘汰时需要用它删哈希表）
        self.val = val  # 存储 value
        self.prev = None  # 前驱指针
        self.next = None  # 后继指针


class LRUCache2:
    # 初始化 LRU 缓存
    def __init__(self, capacity: int):
        self.cap = capacity  # 缓存最大容量
        self.cache = dict()  # 哈希表：key -> Node，O(1) 查找节点

        # 建立虚拟头、虚拟尾节点（哨兵节点，避免空指针判断）
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # 双向链表初始化：head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 私有方法：将节点添加到 **链表头部**（表示最近使用）
    def _add(self, node):
        node.next = self.head.next  # 新节点的 next 指向原来的第一个节点
        node.prev = self.head  # 新节点的 prev 指向虚拟头
        self.head.next.prev = node  # 原来第一个节点的前驱指向新节点
        self.head.next = node  # 虚拟头的 next 指向新节点

    # 私有方法：从双向链表中 **移除指定节点**
    def _remove(self, node):
        prev_node = node.prev  # 取出当前节点的前驱
        next_node = node.next  # 取出当前节点的后继
        prev_node.next = next_node  # 前驱直接连后继
        next_node.prev = prev_node  # 后继直接连前驱

    # 获取 key 对应的 value
    def get(self, key: int) -> int:
        if key not in self.cache:  # key 不存在，返回 -1
            return -1

        node = self.cache[key]  # 从哈希表拿到节点
        self._remove(node)  # 从原来位置删掉
        self._add(node)  # 加到头部，表示刚被访问
        return node.val  # 返回值

    # 插入/更新 key-value
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # 如果 key 已存在
            node = self.cache[key]  # 拿到节点
            node.val = value  # 更新 value
            self._remove(node)  # 移除旧位置
        else:  # key 不存在
            node = Node(key, value)  # 创建新节点
            self.cache[key] = node  # 存入哈希表（你原来这里漏了 = node）

        self._add(node)  # 统一加到头部（最近使用）

        # 如果超过容量，删除最久未使用（尾部节点）
        if len(self.cache) > self.cap:
            lru_node = self.tail.prev  # 最久未使用节点是尾节点的前一个
            self._remove(lru_node)  # 从链表删除
            del self.cache[lru_node.key]  # 同步删除哈希表映射