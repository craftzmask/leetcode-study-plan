class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            if target - num in indices:
                return [i, indices[target - num]]
            else:
                indices[num] = i
        return []