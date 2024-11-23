def check(s):
    c = {'}': '{', ')': '(', ']': '['}
    stack = []
    for i in s:
        if i in c:
            if len(stack) == 0 or stack[-1] != c[i]:
                return False
            stack.pop()
        else:
            stack.append(i)
    return len(stack) == 0

s = input()
if check(s):
    print('yes')
else:
    print('no')
