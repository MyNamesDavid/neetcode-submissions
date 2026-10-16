class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            lookup_result = target - nums[i]
            if lookup_result in my_map:
                return [ my_map[lookup_result], i]
            else:
                my_map[nums[i]] = i
        return []