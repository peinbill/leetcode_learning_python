from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == None:
            return s

        def rever(str, i, j):
            if i >= j:
                return str
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
            rever(str, i, j)

        rever(s, 0, len(s) - 1)
        return s



    def reverseString2(self, s: List[str]) -> None:
        if s == None or len(s)==1:
            return s
        left,right = 0 ,len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return s



