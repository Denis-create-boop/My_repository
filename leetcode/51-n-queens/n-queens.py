class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dvs(x):
            if x == n:
                copy = ls_dot[:]
                sol = []

                for i in copy:
                    sol.append(''.join(i[:]))
                ans.append(sol)
                return
            
            for i in range(n):
                if i in col or x + i in pos or x - i in neg:
                    continue
                
                ls_dot[x][i] = 'Q'
                col.add(i)
                pos.add(x + i)
                neg.add(x - i)

                dvs(x + 1)

                ls_dot[x][i] = '.'
                col.remove(i)
                pos.remove(x + i)
                neg.remove(x - i)

        ls_dot = [["."] * n for _ in range(n)]

        col = set()
        pos = set()
        neg = set()
        ans = []
        dvs(0)

        return ans