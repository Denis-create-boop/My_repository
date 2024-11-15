n = int(input())
arr = list(map(int, input().split()))

mod = 10 ** 9 + 7
pref_sum = [0] * (n + 1)

for i in range(1, n + 1):
    pref_sum[i] = (pref_sum[i - 1] + arr[i - 1]) % mod

suff_sum = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    suff_sum[i] = (suff_sum[i + 1] + arr[i]) % mod

ans = 0

for now_pos in range(1, n - 1):
    ans = (ans + pref_sum[now_pos] * arr[now_pos] * suff_sum[now_pos + 1]) % mod

print(ans)
