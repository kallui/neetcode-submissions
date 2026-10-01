class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r  = 0, 0
        seen = {}
        res = 0
        maxF = 0
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = 1
            else:
                seen[s[r]] += 1
            maxF = max(maxF, seen[s[r]])

            while (r-l+1) - max(seen.values()) > k: 
                seen[s[l]] -=1
                l += 1
            res = max(res, r-l+1)

            r+=1
        
        return res
            


