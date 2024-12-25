class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        for i in range(len(digits)):
            digits[i] = str(digits[i])

        num = int(''.join(digits)) + 1
        for i in str(num):
            res.append(int(i))
        
        return res