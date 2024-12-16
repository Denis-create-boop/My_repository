class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            return x ** n

        result = pow(x, n)
        return result