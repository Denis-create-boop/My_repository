n = int(input())
pref_sum = [0]

for i in range(n):
    s = input()
    if s == '-':
        op = '-'
    else:
        op, num = s[0], int(s[1:])
    if op == '+':
        pref_sum.append(pref_sum[-1] + num)
    if op == '-':
        print(pref_sum[-1] - pref_sum[-2])
        pref_sum.pop()
    if op == '?':
        print(pref_sum[-1] - pref_sum[-num - 1])
