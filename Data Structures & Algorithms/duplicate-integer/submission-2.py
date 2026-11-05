class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Sets can be used to show if there are duplicates
        duplicates = set()

        for num in nums:
            if num in duplicates:
                return True
            duplicates.add(num)
        return False
        