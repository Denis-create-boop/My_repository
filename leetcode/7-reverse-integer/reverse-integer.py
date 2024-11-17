class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if y[0] != '-':
            y1 = y[::-1]
        else:
            x = y[1:]
            y1 = y[0] + x[::-1]
        ans = int(y1)
        if ans > -2 ** 31 and ans < 2 ** 31 - 1:
            return ans

        else:
            return 0