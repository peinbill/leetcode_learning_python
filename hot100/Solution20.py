class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            if i == "}":
                tmp = stack.pop()
                if tmp != "{":
                    return False
            if i == ")":
                tmp = stack.pop()
                if tmp != "(":
                    return False
            if i == "]":
                tmp = stack.pop()
                if tmp != "[":
                    return False
        return len(stack) == 0