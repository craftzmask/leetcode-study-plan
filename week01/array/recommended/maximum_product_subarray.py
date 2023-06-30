class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def product(nums):
            current_product = 1
            max_product = -10**10000
            
            for num in nums:
                current_product *= num
                max_product = max(max_product, current_product)
                if num == 0:
                    current_product = 1
            
            return max_product

        return max(product(nums), product(nums[::-1]))