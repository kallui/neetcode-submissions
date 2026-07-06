class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for x in strs:
            sortedStr = "".join(sorted(x))
            if sortedStr in dic:
                dic[sortedStr].append(x)
            else:
                dic[sortedStr] = [x]

        return list(dic.values())