class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        def isPalindromeStr(x:str):
            if x == "":
                return True
            if x[0] == x[-1]:
                return isPalindromeStr(x[1:-1])
            else:
                return False

        return isPalindromeStr(str(x))