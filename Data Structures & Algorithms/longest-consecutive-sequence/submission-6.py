class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        maxx=1
        nums = set(nums)
        for i in nums:
            temp=i
            counter = 1
            if temp-1 not in nums and temp+1 in nums:
                while temp+1 in nums:
                    counter+=1
                    temp+=1
                    maxx=max(maxx,counter)
        return maxx