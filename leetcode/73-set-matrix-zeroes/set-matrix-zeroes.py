class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ls = []
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    ls.append([i, j])
        if ls:
            for l in ls:
                for i in range(row):
                    for j in range(col):
                        if i == l[0] or j == l[1]:
                            matrix[i][j] = 0

        