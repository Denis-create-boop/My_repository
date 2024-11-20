n = int(input())
alph = input()
s = input()

closing = {')': '(', ']': '['}
stack = []

for c in s:
    if c in closing:
        stack.pop()
    else:
        stack.append(c)

ans = []
for i in range(n - len(s)):
    for c in alph:
        if c in closing and len(stack) > 0 and stack[-1] == closing[c]:
            ans.append(c)
            stack.pop()
            break
        elif c not in closing and n - len(s) - i > len(stack):
            ans.append(c)
            stack.append(c)
            break
print(s + ''.join(ans))
