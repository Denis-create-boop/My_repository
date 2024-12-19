class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False  # Cannot proceed further
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) - 1:
                return True  # Reached or surpassed last index
        return False