
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        rtn_list = [float("inf") for _ in range(amount+1)]
        rtn_list[0] = 0
        for i in range(1,len(rtn_list)):
            for coin in coins:
                if i-coin >=0 and rtn_list[i-coin] != float("inf"):
                    rtn_list[i] = min(rtn_list[i-coin]+1,rtn_list[i])

        if rtn_list[-1] == float("inf"):
            return -1
        else:
            return rtn_list[-1]