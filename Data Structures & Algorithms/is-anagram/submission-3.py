class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        for x in s:
            if x in mp1:
                mp1[x] = mp1[x] + 1
            else:
                mp1[x] = 1

        for x in t:
            if x in mp2:
                mp2[x] = mp2[x] + 1
            else:
                mp2[x] = 1

        return mp1==mp2