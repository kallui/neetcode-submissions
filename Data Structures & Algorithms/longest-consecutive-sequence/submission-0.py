class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: nums = [2,20,4,10,3,4,5] 
        # Output: 4
        numsSet = set(nums)
        longest = 0

        for x in numsSet:
            if x-1 not in numsSet:
                length = 1
                nextNum = x+1
                while nextNum in numsSet:
                    length += 1
                    nextNum += 1
                if length > longest:
                    longest = length
        return longest