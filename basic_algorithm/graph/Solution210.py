# -*- encoding: utf-8 -*-
"""
@File    : Solution210.py
@Time    : 2023/8/9 11:37 下午
@Author  : huangjinyu
@Desc   : 
"""
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 记录后序遍历结果
        postorder = []
        # 记录是否存在环
        hasCycle = [False]
        visited = [False] * numCourses
        onPath = [False] * numCourses

        # 建图函数
        def buildGraph(numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
            # 图中共有 numCourses 个节点
            graph = [[] for _ in range(numCourses)]
            for edge in prerequisites:
                from_, to_ = edge[1], edge[0]
                # 添加一条从 from 指向 to 的有向边
                # 边的方向是「被依赖」关系，即修完课程 from 才能修课程 to
                graph[from_].append(to_)
            return graph

        # 图遍历函数
        def traverse(graph, s):
            if onPath[s]:
                # 发现环
                hasCycle[0] = True
            if visited[s] or hasCycle[0]:
                return
            # 前序遍历位置
            onPath[s] = True
            visited[s] = True
            for t in graph[s]:
                traverse(graph, t)
            # 后序遍历位置
            postorder.append(s)
            onPath[s] = False

        graph = buildGraph(numCourses, prerequisites)
        # 遍历图
        for i in range(numCourses):
            traverse(graph, i)
        # 有环图无法进行拓扑排序
        if hasCycle[0]:
            return []
        # 逆后序遍历结果即为拓扑排序结果
        postorder.reverse()
        res = []
        for i in postorder:
            res.append(i)
        return res