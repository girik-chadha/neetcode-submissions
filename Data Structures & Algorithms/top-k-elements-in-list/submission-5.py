class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        if k == len(list(count.keys())):
            return list(count.keys())

        lst = sorted(count.items(), key =lambda x: x[1])  
        output=[]
        for i in range(len(lst)-1,len(lst)-1-k,-1):
            output.append(lst[i][0])
        return output