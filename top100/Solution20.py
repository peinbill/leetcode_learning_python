# -*- encoding: utf-8 -*-
"""
@File    : Solution20.py
@Time    : 2023/10/7 10:25 下午
@Author  : huangjinyu
@Desc   : 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in set(["(","{","["]):
                stack.append(i)
            else:
                try:
                    top = stack[-1]
                except:
                    return False
                if i =="]" and top == "[":
                    stack.pop()
                elif i == "}" and top == "{":
                    stack.pop()
                elif i==")" and top == "(":
                    stack.pop()

                else:
                    return False


        return len(stack)==0