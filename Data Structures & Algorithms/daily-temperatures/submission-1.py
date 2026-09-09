class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0]*len(temperatures)
        for t in range(len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                    days[stack[-1]] = t-stack[-1]
                    stack.pop()
            stack.append(t)
        return days
                