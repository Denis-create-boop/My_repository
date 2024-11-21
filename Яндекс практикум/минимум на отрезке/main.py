from collections import deque

dq = deque()
n, k = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n):
    if i >= k and nums[i - k] == dq[0]:
        dq.popleft()
    while len(dq) > 0 and dq[-1] > nums[i]:
        dq.pop()
    dq.append(nums[i])
    if i >= k - 1:
        print(dq[0])
