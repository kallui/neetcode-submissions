class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # not sorted so cant do two pointer

        # use hash map
        # add values to hash 1 by 1, and go thru loop, see if we can find the pair
        mp = {}
        for i, v in enumerate(nums):
            first = target - v
            if first in mp:
                return [mp[first], i] #return index
            else:
                mp[v] = i
        return 0,0