from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        解决数独问题的主方法
        参数: board - 9x9的数独棋盘，其中空格用"."表示
        返回值: 无，直接修改输入的board
        """

        def dfs(pos: int):
            """
            深度优先搜索函数，用于尝试填充数独空格
            参数: pos - 当前处理的空格索引
            """
            nonlocal valid  # 声明valid为非局部变量，用于标记是否找到解

            # 如果所有空格都已填充，说明找到了解
            if pos == len(spaces):
                valid = True
                return

                # 获取当前空格的坐标
            i, j = spaces[pos]

            # 尝试填充1-9的数字
            for digit in range(9):
                # 检查当前数字在所在行、列和3x3块中是否已使用
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    # 标记该数字为已使用
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    # 在棋盘上填入数字
                    board[i][j] = str(digit + 1)
                    # 递归处理下一个空格
                    dfs(pos + 1)
                    # 回溯：撤销当前数字的使用标记
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False

                    # 如果找到解，立即返回
                if valid:
                    return

                    # 初始化三个辅助数组，用于记录数字的使用情况

        # line[i][digit]: 标记第i行是否已使用数字digit+1
        line = [[False] * 9 for _ in range(9)]
        # column[j][digit]: 标记第j列是否已使用数字digit+1
        column = [[False] * 9 for _ in range(9)]
        # block[i//3][j//3][digit]: 标记第(i//3, j//3)个3x3块是否已使用数字digit+1
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]

        valid = False  # 标记是否找到解
        spaces = list()  # 存储所有空格的坐标

        # 遍历棋盘，收集空格位置并初始化已使用数字的标记
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    # 记录空格位置
                    spaces.append((i, j))
                else:
                    # 计算数字对应的索引（0-8）
                    digit = int(board[i][j]) - 1
                    # 标记该数字为已使用
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

                    # 从第一个空格开始深度优先搜索
        dfs(0)


