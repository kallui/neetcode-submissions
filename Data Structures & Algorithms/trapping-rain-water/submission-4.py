class Solution:
    def trap(self, height: List[int]) -> int:
        
        #total water between 2 heights
        # water = 

        # keep track of highestLeft and highestRight on a given point
        highestLeft, highestRight = [], []
        maxLeft, maxRight = 0,0
        
        
        i = 0
        while i < len(height):
            highestLeft.append(maxLeft)
            maxLeft = max(maxLeft, height[i])
            i += 1
        
        i = len(height) -1
        while i >= 0:
            highestRight.append(maxRight)
            maxRight = max(maxRight, height[i])
            i-=1
        highestRight.reverse()

        result = 0
        for i, v in enumerate(height):
            water = max(min(highestLeft[i],highestRight[i]) - v,0)
            result += water
        
        return result