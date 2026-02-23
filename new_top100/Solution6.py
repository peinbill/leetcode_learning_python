from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        row_dict = defaultdict(list)
        i, flag = 0, -1
        for c in s:
            row_dict[i].append(c)
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        std = ""
        for i in range(numRows):
            std += "".join(row_dict[i])
        return std