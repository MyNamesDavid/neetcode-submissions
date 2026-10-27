
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        s1_state = {}

        for c in s1:
            s1_state[c] = s1_state.get(c, 0) + 1

        state = {}
        s1_length = len(s1)

        for end in range(len(s2)):
            state[s2[end]] = state.get(s2[end], 0) + 1

            while end - start + 1 > s1_length:
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1

            if end - start + 1 == s1_length and state == s1_state:
                return True

        return False
