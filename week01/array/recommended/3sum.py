class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triple = (nums[i], nums[j], nums[k])
                    ans.add(triple)
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        
        return ans