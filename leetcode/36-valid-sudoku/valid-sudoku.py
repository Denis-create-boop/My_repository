class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ls_cols = []
        ls_block = []
        def check_line(l):
            flag_line = True
            for i in l:
                line = []
                for j in i:
                    if j.isdigit():
                        line.append(j)
                line.append('.')
                if len(set(line)) == len(line):
                    flag_line = True
                else:
                    flag_line = False
                    break
            return flag_line

        def check_blocks(block):
            flag_line = True
            ans = []
            for i in block:
                for j in i:
                    for c in j:
                        if c.isdigit():
                            ans.append(c)
                if len(set(ans)) != len(ans):
                    flag_line = False
                    break
                ans = []
            return flag_line

        def create_block(n, ls_block, a, b, c):
            ls_block[n].append([board[i][a], board[i][b], board[i][c]])
            ls_block[n].append([board[i+1][a], board[i+1][b], board[i+1][c]])
            ls_block[n].append([board[i+2][a], board[i+2][b], board[i+2][c]])


        for i in range(0, 9):
            for j in range(0, 9):
                ls_cols.append([])
                ls_cols[i].append(board[j][i])

        for i in range(0, 7, 3):
            ls_block.append([])
            ls_block.append([])
            ls_block.append([])
            a, b, c = 0, 1, 2
            r = i
            for _ in range(3):

                create_block(r, ls_block, a, b, c)
                a += 3
                b += 3
                c += 3
                r += 1



        flag_line = check_line(board)
        if flag_line:
            flag_line = check_line(ls_cols)
        if flag_line:
            flag_line = check_blocks(ls_block)

        return flag_line
