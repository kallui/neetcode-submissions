class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        # sliding window but more optimal with a map
        # map stores indexes of the last appearanace of a char
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1) # move l to after s[r]
            
            mp[s[r]] = r
        
            res = max(res, r - l + 1)

        return res
