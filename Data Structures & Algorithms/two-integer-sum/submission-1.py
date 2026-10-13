class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=0
        while count<len(nums):
            for i in range(count+1,len(nums)):
                if nums[count]+nums[i]==target:
                    return [count,i]
            count+=1
        