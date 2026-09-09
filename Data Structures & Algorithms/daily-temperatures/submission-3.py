class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]*len(temperatures)
        track = []
        for i,temp in enumerate(temperatures):
            if track:
                while track and temp>track[-1][0]:
                    t, index = track.pop()
                    stack[index] = i-index
            track.append([temp, i])
        return stack

