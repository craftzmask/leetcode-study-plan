class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        l, r = 0, len(height) - 1
        while l <= r:
            amount = min(height[l], height[r]) * (r - l)
            max_amount = max(max_amount, amount)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_amount