class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        state = set()
        max_result = 0

        for end in range(len(s)):
            
            while s[end] in state:
                state.remove(s[start])
                start+=1
            state.add(s[end])
            max_result = max(max_result, end - start + 1)
        return max_result

