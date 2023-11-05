# -*- encoding: utf-8 -*-
"""
@File    : Solution17.py
@Time    : 2023/10/7 10:24 下午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 回溯方法的应用

        @param digits:
        @return:
        """
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations