
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        num_set = set(nums)

        for num in nums:
            current_num = num
            
            if num - 1 not in num_set: 
                longest = 1  
                while (current_num + 1) in num_set:
                    longest+=1
                    current_num+=1
                result = max(result, longest)
                
        return result
