class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_1 = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs",
        "8":"tuv", "9":"wxyz"}
        if not digits:
            return []
        result = [""]
        for x in digits:
            temp = []
            for a in result:
                for j in dict_1[x]:
                    temp.append(a + j)
            result = temp
        
        return result
        
