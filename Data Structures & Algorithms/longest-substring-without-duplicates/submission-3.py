class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        seen = set()

        
        res = 0
        if len(s) > 0:
            seen.add(s[l])
            res += 1
        
        #Input: s = "zxyzxyz"
        # "xx"
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            else:
                seen.add(s[r])

            r += 1
            res = max(res, len(seen))
        return res