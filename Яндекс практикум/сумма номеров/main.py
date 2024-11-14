n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = {0: 1}
now_sum = 0
ans = 0

for now in arr:
    now_sum += now
    ans += cnt.get(now_sum - k, 0)
    cnt[now_sum] = cnt.get(now_sum, 0) + 1

print(ans)
