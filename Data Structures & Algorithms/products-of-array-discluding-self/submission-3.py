class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        suffix = 1
        preList = []
        sufList = []

        for i, v in enumerate(nums):
            preList.append(prefix)
            sufList.append(suffix) 
            prefix = prefix * v
            suffix = suffix * nums[len(nums)-1-i]
            
        res = []
        for i in range(len(nums)):
            res.append(preList[i] * sufList[len(nums)-1-i])

        return res

