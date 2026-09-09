class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, len(numbers)-1
        for n in range(len(numbers)):
            sum = numbers[r]+numbers[l]
            if sum == target: return [r+1,l+1]
            elif sum > target: l-=1
            else: r+=1
        

