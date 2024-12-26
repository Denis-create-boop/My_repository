class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for i in matrix:
            if target in i:
                flag = True
                break

        return flag