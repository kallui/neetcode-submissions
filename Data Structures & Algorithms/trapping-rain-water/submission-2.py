class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        # ex: [0,1,0,2,1,0,1,3,2,1,2,1]
        # [4,2,0,3,2,5]
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water = maxLeft - height[l]
                if water < 0:
                    water = 0
                res += water
                
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water = maxRight - height[r]
                if water < 0:
                    water = 0
                res += water

        return res