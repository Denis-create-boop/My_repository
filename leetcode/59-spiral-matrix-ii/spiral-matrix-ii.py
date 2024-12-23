class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        mat = [[0] * int(n) for i in range(n)]

        c = 1        
        a, b = 0, 0
        rows = n - 1
        cols = n - 1

        while a <= cols and b <= rows:
            for i in range(a, cols + 1):
                mat[a][i] = c
                c += 1
            b += 1
            for i in range(b, rows + 1):
                mat[i][cols] = c
                c += 1
            cols -= 1
            if b <= rows:
                for i in range(cols, a-1, -1):
                    mat[rows][i] = c
                    c += 1
                rows -= 1
            if a <= cols:
                for i in range(rows, b-1, -1):
                    mat[i][a] = c
                    c += 1
                a += 1
        return mat
    