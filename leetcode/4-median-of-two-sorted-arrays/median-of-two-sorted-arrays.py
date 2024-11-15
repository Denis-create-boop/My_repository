class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        for i in nums1:
            ans.append(i)
        for i in nums2:
            ans.append(i)
        ans = sorted(ans)
        if len(ans) % 2 != 0:
            return ans[len(ans) // 2]
        else:
            return (ans[len(ans) // 2] + ans[len(ans) // 2 - 1]) / 2