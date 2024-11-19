class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = set()
        result = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tempsum = nums[i] + nums[j] + nums[k]
                if tempsum == 0:
                    temp.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tempsum < 0:
                    j += 1
                else:
                    k -= 1
        result = list(temp)
        return result