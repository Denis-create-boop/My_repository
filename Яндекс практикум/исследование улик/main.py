n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))

left = 0
ans = [0] * n
moves = 0

for right in range(1, n):
    if a[right] == a[right - 1]:
        if moves < k:
            moves += 1
        else:
            while moves >= k:
                if a[left] == a[right + 1]:
                    moves -= 1
                left += 1
            moves += 1
    elif a[right] < a[right - 1]:
        left = right
        moves = 0
    ans[right] = left

to_print = []
for idx in x:
    to_print.append(ans[idx - 1] + 1)

print(to_print)
