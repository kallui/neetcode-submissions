class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for i, v in enumerate(nums):
            first = target - v

            if first not in mp:
                mp[v] = i
            else:
                return [mp[first], i]
