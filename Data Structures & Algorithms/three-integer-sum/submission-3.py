class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        
        # outer
        nums.sort()
        for i, v in enumerate(nums):
            l = i+1
            r = len(nums)-1

            while l < r:
                total = v + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0: 
                    r -=1
                elif total == 0:
                    result.add((v,nums[l],nums[r]))
                    l +=1
                    r -=1


        return [list(value) for value in result]