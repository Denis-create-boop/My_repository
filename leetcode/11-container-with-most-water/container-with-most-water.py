class Solution:
    def maxArea(self, height: List[int]):        
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            result = min(height[left], height[right]) * (right - left)
            ans = max(ans, result)

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        return ans