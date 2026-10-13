from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict=defaultdict(int)
        for i in range(len(nums)):
            nums_dict[nums[i]]+=1

        for i in nums_dict:
            if nums_dict.get(i) == 1:
                return i