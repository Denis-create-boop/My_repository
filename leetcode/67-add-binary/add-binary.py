class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a, 2) + int(b, 2)
        ans = bin(res)
        return ans[2:]