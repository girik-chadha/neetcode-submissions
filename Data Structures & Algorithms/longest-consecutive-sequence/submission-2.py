class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0

        sett=set(nums)
        longest=0
        for num in sett:
            if num-1 not in sett:
                length=1
                next_num=num+1
                while next_num in sett:
                    length+=1
                    next_num+=1
                longest=max(longest,length)
        return longest


