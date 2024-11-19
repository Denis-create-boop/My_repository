class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = set()
        ans = []
    
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                a = nums[i] + nums[j] + nums[k]
                if a == 0:
                    d.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif a < 0:
                    j += 1
                else:
                    k -= 1
        ans = list(d)
        return ans