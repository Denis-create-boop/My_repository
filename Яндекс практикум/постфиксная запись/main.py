def solve(vr):
    ls = []
    for w in vr:
        if w.isdigit():
            ls.append(int(w))
        else:
            y = ls.pop()
            x = ls.pop()
            z = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y }[w](x, y)
            ls.append(z)
    return ls.pop()

vr = input().split()
print(solve(vr))
