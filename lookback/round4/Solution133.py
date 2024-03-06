#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/2/20 00:33
# @Author      : Jim
# @File        : Solution133.py
# @Software    : PyCharm
# @Description :可以使用dfs，也可以使用bfs，但核心在于不虚

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:


    def __init__(self) -> None:
        self.visited = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if node not in self.visited:
                new_node = Node(val = node.val)
                self.visited[node] = new_node

                for i in node.neighbors:
                    new_node.neighbors.append(dfs(i))
            else:
                new_node = self.visited[node]

            return new_node

        if node is None:
            return None
        new_node = dfs(node)
        return new_node