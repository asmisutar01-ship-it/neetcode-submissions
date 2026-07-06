class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for i in strs :
            key = " ".join(sorted(i))
            ana[key].append(i)
        return list(ana.values())
