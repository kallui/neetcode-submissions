class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        mp = {} # counter
        for c in s1:
            if c in mp:
                mp[c] += 1
            else:
                mp[c] = 1

        for r in range(len(s2)):
            if (r-l+1) > len(s1):
                if s2[l] in mp:
                    mp[s2[l]] +=1
                l += 1
            if s2[r] in mp:
                mp[s2[r]] -= 1

            if (r-l+1) == len(s1) and all(v == 0 for v in mp.values()):
                return True
            
        return False

