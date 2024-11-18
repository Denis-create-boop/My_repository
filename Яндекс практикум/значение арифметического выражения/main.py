s = input()

def is_aryf(s):  
    if s[0] == '-':
        ls = [0]  
        num = '0'

    else:
        ls = []
        num = ''
    count_a = 0
    count_b = 0

    flag = True

    if s[0] not in '+*/)' and s[-1] not in '*-+/(':
        for i in s:
            if ls:
                if i.isdigit() and not type(ls[-1]) is int and ls[-1] != ')':
                    num += i
                elif i in '+*/':
                    if num:
                        ls.append(int(num))
                        num = ''
                    else:
                        if ls[-1] == '(':
                            flag  = False
                            break

                    ls.append(i)
                elif i == '-':
                    if num:
                        ls.append(int(num))
                        num = ''
                    elif ls[-1] == '(':
                        ls.append(0)
                    ls.append(i)
                    
                elif i == '(' and ls[-1] in '+-*/(':
                    count_a += 1
                    ls.append(i)
                    
                elif i == ')' and count_a > count_b and ((type(ls[-1]) is int or ls[-1] == ')') or (ls[-1] in '-+*/(' and num)):
                    count_b += 1
                    if num:
                        ls.append(int(num))
                        num = ''
                    ls.append(i)
                elif i == ' ':
                    if num:
                        ls.append(int(num))
                        num = ''
                    continue
                
                else:
                    flag = False
                    break

            else:
                if num and i.isdigit():
                    num += i
                elif num == '' and i.isdigit():
                    num += i 
                elif i == '(':
                    count_a += 1
                    if num:
                        ls.append(int(num))
                        num = ''
                    ls.append(i)
                elif num and i == ' ':
                    ls.append(int(num))
                    num = ''
                elif i in '+-*/':
                    ls.append(int(num))
                    num = ''
                    ls.append(i)
                

    else:
        flag = False

    if num:
        ls.append(int(num))
    if count_a != count_b:
        flag = False
    if flag:
        return ls
    else:
        return 'WRONG'

    

def infic(s):
    stack = []
    ans = []
    d = {'-': 0, '+': 0, '*': 1, '/': 1}
    for i in s:
        if type(i) is int:
            ans.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while stack and  stack[-1] != '(' and d[stack[-1]] >= d[i]:
                    ans.append(stack.pop())
                stack.append(i)
    if stack:
        while stack:
            ans.append(stack.pop())
    return ans


def solve(vr):
    ls = []
    for w in vr:
        if type(w) is int:
            ls.append(w)
        else:
            y = ls.pop()
            x = ls.pop()
            z = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y }[w](x, y)
            ls.append(z)
    return ls.pop()

a = is_aryf(s)

if a != 'WRONG':
    s = infic(a)
    print(solve(s))
else:
    print(a)
