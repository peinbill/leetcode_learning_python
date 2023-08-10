# -*- encoding: utf-8 -*-
"""
@File    : Solution773.py
@Time    : 2023/8/8 8:40 下午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List,Generator
from collections import deque
class Solution:
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            x = s.index("0")
            for y in Solution.NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                yield "".join(s)
                s[x], s[y] = s[y], s[x]

        initial = "".join(str(num) for num in sum(board, []))
        if initial == "123450":
            return 0

        q = deque([(initial, 0)])
        seen = {initial}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen:
                    if next_status == "123450":
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)

        return -1

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbors = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}

        start = tuple(board[0] + board[1])
        target = tuple([1,2,3,4,5,0])
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            node,depth = queue.popleft()
            if node == target:
                return depth
            pos = node.index(0)
            for i in neighbors[pos]:
                newboard = list(node)
                newboard[pos] = newboard[i]
                newboard[i] = 0
                nb = tuple(newboard)
                if nb not in seen:
                    seen.add(nb)
                    queue.append((nb,depth+1))
        return -1