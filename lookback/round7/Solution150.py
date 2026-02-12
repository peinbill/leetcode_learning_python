from collections import deque
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol = ["+","-","*","/"]
        stack = list()
        for i in tokens:
            if i in symbol:
                first_num = int(stack.pop())
                second_num = int(stack.pop())
                if i == "+":
                    num = first_num + second_num
                elif i == "-":
                    num = second_num-first_num
                elif i == "*":
                    num = first_num * second_num
                elif i == "/":
                    num = second_num / first_num
                stack.append(num)

            else:
                stack.append(i)

        return int(stack.pop())