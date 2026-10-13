class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = {}
        for c in t:
            if c in mp:
                mp[c] += 1
            else:
                mp[c] = 1
        
        l = 0
        res = ""
        for r in range(len(s)):
            if s[r] in mp:
                mp[s[r]] -=1

            # if all of t exist in substring already, can start considering shrinking.
            while all(v <= 0 for v in mp.values()) and l < len(s):
                if (r-l+1) < len(res) or len(res) == 0:
                    res = s[l:r+1]
                if s[l] in mp:
                    mp[s[l]] += 1
                l+=1
            
        return res

