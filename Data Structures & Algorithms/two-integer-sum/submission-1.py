class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup in num_dict:
                return [num_dict[lookup], i]
            num_dict[nums[i]] = i

        return []
