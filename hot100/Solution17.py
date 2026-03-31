from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def brack_track(index: int):
            if len(tmp_collection) == len(digits):
                collections.append("".join(tmp_collection))
            else:
                digit = digits[index]
                words = number_dict[digit]

                for i in words:
                    tmp_collection.append(i)
                    brack_track(index + 1)
                    tmp_collection.pop()

        collections = []
        tmp_collection = []
        brack_track(0)
        return collections