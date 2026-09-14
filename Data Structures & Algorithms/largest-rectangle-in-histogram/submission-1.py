class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights = [7,1,7,2,2,4]
        stack = []  # pair of (height, index)
        n = len(heights)

        maxArea = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][0] > v:
                height, index = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)
                start = index
            stack.append((v, start))

        for h, i in stack:
            area = h * (n-i)
            maxArea = max(maxArea,area)

        return maxArea