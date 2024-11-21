n, b = map(int, input().split())
a = list(map(int, input().split()))

inq = ans = 0

for now in a:
    inq += now
    ans += inq
    inq -= min(inq, b)

ans += inq
print(ans)
