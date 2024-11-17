n = int(input())
nums = list(map(int, input().split()))

ans = [-1] * n
stack = []

for i in range(n):
    while len(stack) > 0 and nums[i] < stack[-1][0]:
        ans[stack[-1][1]] = i
        stack.pop()
    stack.append((nums[i], i))

print(*ans)
