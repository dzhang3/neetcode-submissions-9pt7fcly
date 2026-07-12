class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(Counter(s).items()))].append(s)
            # print(tuple(sorted(Counter(s).items())))
        return list(anagrams.values())