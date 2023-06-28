class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = None
        largest_sum = None

        for num in nums:
            if current_sum is None:
                current_sum = num
                largest_sum = num
            else:
                current_sum = max(current_sum + num, num)
                largest_sum = max(largest_sum, current_sum)

        return largest_sum