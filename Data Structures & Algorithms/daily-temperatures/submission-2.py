class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # tuple (temperature, index)

        for i, v in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < v:
                temp, index = stack.pop()
                result[index] = i-index
            stack.append((v, i))
        
        return result