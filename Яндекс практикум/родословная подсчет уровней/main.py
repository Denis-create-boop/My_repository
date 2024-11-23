n = int(input())
child_parents = {}

for _ in range(1, n):
    child, parent = input().split()
    child_parents[child] = parent

all_men = set(child_parents.keys()) | set(child_parents.values())
ans = {}

def count_parents(name):
    if name not in child_parents:
        ans[name] = 0
        return 0
    
    parent = child_parents[name]
    if parent in ans:
        value = ans[parent] + 1
    else:
        value = count_parents(parent) + 1
    ans[name] = value
    return value


for name in all_men:
    if name not in ans:
        count_parents(name)

for name in sorted(ans):
    print(name, ans[name])
