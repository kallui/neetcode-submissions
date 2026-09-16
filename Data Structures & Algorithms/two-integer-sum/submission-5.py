class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        
        for i, v in enumerate(nums):
            first = target - v
            if first in mp:
                return [mp[first], i]
            mp[v] = i
            
        return [0,0]