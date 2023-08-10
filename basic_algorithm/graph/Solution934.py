# -*- encoding: utf-8 -*-
"""
@File    : Solution934.py
@Time    : 2023/8/6 11:49 下午
@Author  : huangjinyu
@Desc   :
1. 我们通过遍历找到数组 grid 中的 1 后进行广度优先搜索，此时可以得到第一座岛的位置集合，记为 island，并将其位置全部标记为 −1。
2. 随后我们从 island 中的所有位置开始进行广度优先搜索，当它们到达了任意的 1时，即表示搜索到了第二个岛，搜索的层数就是答案。

、
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v != 1:
                    continue
                island = []
                grid[i][j] = -1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    island.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            q.append((nx, ny))

                step = 0
                q = island
                while True:
                    tmp = q
                    q = []
                    for x, y in tmp:
                        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                            if 0 <= nx < n and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step
                                if grid[nx][ny] == 0:
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
                    step += 1

        return step