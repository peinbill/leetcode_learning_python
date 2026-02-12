def isBadVersion(num:int):
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 0,n
        while left +1 <right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        if isBadVersion(left):
            return left
        return right