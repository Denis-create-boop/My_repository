a, b, c = int(input()), int(input()), int(input()) # кирпич a*b*c
d, e = int(input()), int(input()) # размер отверстия d*e
if a <= d and b <= e or a <= e and b <= d:
    print('YES')

elif c <= d and b <= e or c <= e and b <= d:
    print('YES')

elif a <= d and c <= e or a <= e and c <= d:
    print('YES')

else:
    print('NO')
