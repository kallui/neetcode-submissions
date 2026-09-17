class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        mp = {}
        while r < len(s):
            
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r # save final appearance index
            res = max(res, r-l+1)
            r+=1
        return res
                

