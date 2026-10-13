class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1=dict()
        for i in range(0,len(nums)):
            dict1[nums[i]]=i
        fake_target=0
        for i in range(0,len(nums)):
            y=target-nums[i]
            if y in dict1.keys() and dict1[y]!=i:
                return [i,dict1[y]]