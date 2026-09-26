class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        mp = {}
        res = 0
        while r < len(s):
            if s[r] not in mp:
                mp[s[r]] = r
            else:
                l = max(l, mp[s[r]] + 1)
                mp[s[r]] = r
            res = max(res, r-l+1)
            r +=1
        return res