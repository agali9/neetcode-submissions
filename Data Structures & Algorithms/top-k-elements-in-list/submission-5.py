class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        ans = []
        for x in range(len(buckets)-1,0,-1):
            for n in buckets[x]:
                ans.append(n)
            if len(ans) == k: break
        return ans