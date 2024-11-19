class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {
            'I': 1,
            'V': 5,    "IV": 4,
            "X": 10,   "IX": 9,
            "L": 50,   "XL": 40,
            "C": 100,  "XC": 90,
            "D": 500,  "CD": 400,
            "M": 1000, "CM": 900,
        }
        
        ans = 0
        left = 0
        while left < len(s):
            if s[left:left+2] in num_map:
                ans += num_map[s[left:left+2]]
                left += 2
            else:
                ans += num_map[s[left]]
                left += 1

        return ans