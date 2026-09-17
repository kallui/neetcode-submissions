class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dic= {
            ']': '[',
            '}': '{',
            ')': '(',
        }

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        