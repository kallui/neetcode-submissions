class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suffix = 1
        prefix = 1
        prefixList = []
        suffixList = []
        # nums: [1,2,3,4]
        # prefix: [1,1,2,6]
        # suffix: [24, 12, 4, 1]
        for i, x in enumerate(nums):
            prefixList.append(prefix)
            suffixList.append(suffix)
            prefix *= x
            suffix *= nums[len(nums)-i-1]
        
        result = []
        for i, x in enumerate(prefixList):
            tmp = int(x*suffixList[len(suffixList)-i-1])
            result.append(tmp)
        return result