class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # tuple (temperature, index)

        for i, v in enumerate(temperatures):
            if len(stack) > 0:
                # ex: [31,30,29] <- 31
                while len(stack) > 0 and stack[-1][0] < v:
                    result[stack[-1][1]] = i-stack[-1][1]
                    stack.pop()
            stack.append((v, i))
        
        return result