class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x_str = str(x)[1:]
        else:
            x_str = str(x)

        stack = []
        for i in x_str:
            stack.append(int(i))

        std = 0
        while stack:
            std = std * 10 + stack.pop()

        if negative:
            std = -std

        return 0 if std > pow(2, 31) - 1 or std < -pow(2, 31) else std