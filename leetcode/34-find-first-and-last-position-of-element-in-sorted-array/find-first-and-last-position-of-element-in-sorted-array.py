class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

        if ans:
             return [ans[0], ans[-1]]
        else:
            return [-1, -1]