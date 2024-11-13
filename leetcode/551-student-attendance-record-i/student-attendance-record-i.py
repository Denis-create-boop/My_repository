class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        for i in s:
            if L >= 3:
                break
            else:
                if i == 'A':
                    A += 1
                    L = 0
                elif i == 'L':
                    L += 1
                else:
                    L = 0
        if A < 2 and L < 3:
            return True
        else:
            return False