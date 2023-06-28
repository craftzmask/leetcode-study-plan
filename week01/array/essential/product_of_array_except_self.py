class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            prefix.append(product)

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= product
            product *= nums[i]

        return prefix