class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        items = count.items()
        items=sorted(items, key=lambda x: x[1])
        t=k
        for i in range(len(items)-1,-1,-1):
            output.append(items[i][0])
            t=t-1
            if t==0:
                break
        return output


