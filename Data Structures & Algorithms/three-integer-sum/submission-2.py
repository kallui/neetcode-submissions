class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Input: nums = [-1,0,1,2,-1,-4]
        # Output: [[-1,-1,2],[-1,0,1]]

        res = []
        nums.sort()
        
        # sorted = [-4, -1,-1 ,1,2]
        
        for i, v in enumerate(nums):
            # v = first value, if positive, break out loop cus no more possible combos
            if v > 0:
                break
            # if v is duplicate (same number as nums[i-1], skip cus was already considered)
            if i > 0 and v == nums[i-1]:
                continue;

            #else, use v as first value, and use left, right pointer and perform "twosum"
            l, r = i+1, len(nums)-1

            while l < r:
                sum = v + nums[l] + nums[r]

                if sum == 0:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
        
        return res
