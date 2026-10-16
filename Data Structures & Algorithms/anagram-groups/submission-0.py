class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            anagram_map[sortedString].append(strs[i])
        return list(anagram_map.values())
