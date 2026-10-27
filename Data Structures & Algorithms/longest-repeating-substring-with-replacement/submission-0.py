class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        state = {}
        max_result = 0
        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1

            while (end - start + 1) - max(state.values()) > k:
                state[s[start]] -= 1
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1
            max_result = max(max_result, end - start + 1)
            

        return max_result
        