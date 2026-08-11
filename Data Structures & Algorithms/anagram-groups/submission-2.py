class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        mp = {} # "act" : ["act" "cat"] i think
        for x in strs:
            # sort string
            tmp = "".join(sorted(x)) # convert to str

            if tmp in mp:
                mp[tmp].append(x)
            else:
                mp[tmp] = [x]
        
        return list(mp.values())