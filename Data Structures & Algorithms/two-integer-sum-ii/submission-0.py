class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = 0
        for n in range(len(numbers)):
            if (target - numbers[n]) in numbers:
                idx1 = n+1
                idx2 = numbers.index(target - numbers[n])+1
                break
        return [idx1,idx2]