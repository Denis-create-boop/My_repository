class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jump = 0
        count = 0
        total = 0
        for i in range(n - 1):
            total = max(total, i + nums[i])
            if i == count:
                jump += 1
                count = total
        return jump