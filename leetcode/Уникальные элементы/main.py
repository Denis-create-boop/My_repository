def main():
    
    d = {}
    count = 0
    n = int(input())
    ls = list(map(int, input().split()))
    for i in ls:
        d[i] = d.get(i, 0) + 1

    for k, v in d.items():
        if v == 1:
            count += 1

    print(count)
    


if __name__ == '__main__':
    main()
