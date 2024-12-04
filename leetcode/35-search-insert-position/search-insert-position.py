class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = True
        if target in nums:
            return nums.index(target)
        
        else:
            for i in range(len(nums) - 1):
                if nums[i] < target and nums[i + 1] > target:
                    return i + 1
                    flag = False
                    break
            if flag:
                if target > nums[-1]:
                    return len(nums)
                if target < nums[0]:
                    return 0