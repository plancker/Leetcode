class Solution:
    def isValid(self, s: str) -> bool:

        d = {"{": "}", "[": "]", "(": ")"}

        stack = []

        i = 0

        while i < len(s):
            if s[i] not in d.keys():
                if len(stack) > 0 and s[i] == d[stack[len(stack) - 1]]:
                    stack.pop()
                    i = i + 1
                else:
                    return False
            else:
                stack.append(s[i])
                i = i + 1

        if len(stack) == 0:
            return True
        else:
            return False

X = Solution
print(X.isValid(X, "{([({})])}(([[]])))"))
