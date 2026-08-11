class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # create list by default if key doesnt exist yet

        for x in strs:
            tmp = "".join(sorted(x))
            res[tmp].append(x)

        return list(res.values())