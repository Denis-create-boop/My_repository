class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in d.values():
                stack.append(i)
            else:
                if stack and i in d:
                    if stack[-1] == d[i]:
                        stack.pop()
                    else:
                        return False
                        break
                else:
                    return False
                    break
        if len(stack) == 0:
            return True
        else:
            return False