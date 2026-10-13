class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sett=set()
        for i in range(len(nums)+1):
            sett.add(i)
            
        for i in sett:
            if i not in nums:
                return i