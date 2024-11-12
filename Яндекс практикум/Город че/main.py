n, r = map(int, input().split())
arr = list(map, int, input().split())

ans = 0
left = 0
right = 0

while left < n and right < n:
    while right < n and arr[right] - arr[left] <= r:
        right += 1

    ans += n - right
    left += 1

print(ans)
